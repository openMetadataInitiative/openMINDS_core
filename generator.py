#   Copyright (c) 2018, EPFL/Human Brain Project PCO
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import copy
import glob
import json
import os
import re
import shutil
from typing import Optional

TEMPLATE_PROPERTY_TYPE = "_type"
TEMPLATE_PROPERTY_EXTENDS = "_extends"
TEMPLATE_PROPERTY_LINKED_TYPES = "_linkedTypes"


class Generator(object):

    @staticmethod
    def _merge_json(source, extension, properties_to_deep_merge):
        for extension_key in extension:
            if extension_key not in source:
                source[extension_key] = extension[extension_key]
            if extension_key in properties_to_deep_merge and extension_key in source:
                if type(source[extension_key]) is list and type(extension[extension_key]) is list:
                    source[extension_key] = source[extension_key]+extension[extension_key]
                elif type(source[extension_key]) is dict and type(extension[extension_key]) is dict:
                    for property_key in extension[extension_key]:
                        if property_key not in source[extension_key]:
                            source[extension_key][property_key] = extension[extension_key][property_key]

    def _process_schema(self, source_dir, schema_path, version: str, schema: dict) -> Optional[dict]:
        if TEMPLATE_PROPERTY_TYPE not in schema:
            print(f"Skipping schema {schema_path} since it doesn't contain a type definition")
            return None

        if TEMPLATE_PROPERTY_EXTENDS in schema:
            extension_path = os.path.abspath(os.path.join(source_dir, schema[TEMPLATE_PROPERTY_EXTENDS]))
            # Make sure that the extension path is part of the source directory (because _extends could
            # include path navigation directives such as "..")
            if extension_path.startswith(source_dir):
                with open(extension_path, "r") as extension_file:
                    extension = json.load(extension_file)
                self._merge_json(schema, extension, ["properties", "required"])
            del schema[TEMPLATE_PROPERTY_EXTENDS]

        schema["$schema"] = "http://json-schema.org/draft-07/schema#"

        required = schema["required"] if "required" in schema else []
        required.append("@id")
        required.append("@type")
        schema["required"] = list(set(required))

        if "properties" not in schema:
            schema["properties"] = {}

        if "additionalProperties" not in schema:
            schema["additionalProperties"] = False

        properties = schema["properties"]
        properties["@id"] = {
            "type": "string",
            "description": "Metadata node identifier."
        }
        if TEMPLATE_PROPERTY_TYPE in schema:
            schema_id = self._type_to_schema_id(version, schema[TEMPLATE_PROPERTY_TYPE])
            schema["$id"] = schema_id
            schema["type"] = "object"
            properties["@type"] = {"type": "string", "const": schema[TEMPLATE_PROPERTY_TYPE]}
        return schema

    @staticmethod
    def _relative_path_from_schema_id(schema_id):
        first_level = os.path.basename(os.path.dirname(schema_id))
        second_level = os.path.basename(os.path.dirname(first_level))
        return f"{second_level}/{first_level}/{os.path.basename(schema_id)}"

    @staticmethod
    def _type_to_schema_id(version, t):
        type_base = os.path.dirname(t)
        type_name = os.path.basename(t)
        schema_name = type_name[0].lower()+type_name[1:]
        return f"{type_base}/{version}/{schema_name}.schema.json"

    @staticmethod
    def _clear_template_properties(schema):
        if TEMPLATE_PROPERTY_TYPE in schema:
            del schema[TEMPLATE_PROPERTY_TYPE]

    @staticmethod
    def _resolve_jsonschema_templates(properties):
        for property_key in properties:
            property = properties[property_key]
            if TEMPLATE_PROPERTY_LINKED_TYPES in property:
                if "type" not in property:
                    # Make sure, that a type is defined - let's default to object
                    property["type"] = "object"
                target = property

                if property["type"] == "array":
                    target = {}
                    property["items"] = target

                target["if"] = {"required": ["@type"]}
                target["then"] = {
                    "properties": {
                        "@id": {
                            "type": "string",
                            "format": "iri"
                        },
                        "@type": {
                            "type": "string",
                            "format": "iri",
                            "enum": property[TEMPLATE_PROPERTY_LINKED_TYPES]
                        }},
                    "required": ["@id"]
                }
                target["else"] = {
                    "properties": {
                        "@id": {
                            "type": "string",
                            "format": "iri"
                        }
                    },
                    "required": ["@id"]
                }
                del property[TEMPLATE_PROPERTY_LINKED_TYPES]

    @staticmethod
    def _do_generate_html(version, schema):
        typename = schema['_type']
        simple_typename = os.path.basename(typename)

        properties = []
        for p in sorted(schema["properties"]):
            property = schema["properties"][p]

            if TEMPLATE_PROPERTY_LINKED_TYPES in property:
                linked_types_links = [f"<a href=\"{Generator._type_to_schema_id(version, linked_type)}.html\">"
                                      f"{os.path.basename(linked_type)}"
                                      f"</a>" for linked_type in property['_linkedTypes']]
                if "type" in property and property["type"] == "array":
                    type = f"Array of relations to {' or '.join(linked_types_links)}"
                else:
                    type = f"Relation to {' or '.join(linked_types_links)}"
            elif "type" in property and "format" in property:
                type = f"{property['type']} ({property['format']})"
            elif "type" in property:
                type = property['type']
            else:
                type = "unknown"

            properties.append(f"<tr><td class=\"property\">{p}</td><td>{type}</td>"
                              f"<td>{property['description'] if 'description' in property else ''}</tr>")
        properties_table = f"<table>{''.join(properties)}</table>"
        return f"<html> <head><link rel=\"stylesheet\" href=\"../style.css\"></head>" \
               f"<body><h1>{simple_typename}</h1>" \
               f"<h3>{typename} - <a href=\"{os.path.basename(Generator._type_to_schema_id(version, typename))}\">" \
               f"JSON Schema</a></h3>" \
               f"{properties_table}</body></html>"

    def _generate_jsonschema(self, processed_schema, target_path):
        schema = copy.deepcopy(processed_schema)
        self._resolve_jsonschema_templates(schema["properties"])
        self._clear_template_properties(schema)
        if not os.path.exists(os.path.dirname(target_path)):
            os.makedirs(os.path.dirname(target_path))
        with open(target_path, "w") as target_file:
            target_file.write(json.dumps(schema, indent=4))

    def _generate_html(self, version, processed_schema, target_path):
        if not os.path.exists(os.path.dirname(target_path)):
            os.makedirs(os.path.dirname(target_path))
        with open(target_path, "w") as target_file:
            target_file.write(self._do_generate_html(version, processed_schema))

    def generate(self):
        for source_dir in glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), '**/v*'), recursive=True):
            if re.match(".*/v\\d\\.\\d", str(source_dir)) and "target/v" not in source_dir:
                version_number = os.path.basename(source_dir)
                target_dir = os.path.join(os.path.dirname(source_dir), "target", version_number)
                if os.path.exists(target_dir):
                    shutil.rmtree(target_dir)
                for schema_path in glob.glob(os.path.join(source_dir, '**/*.schema.json'), recursive=True):
                    file_name = schema_path[len(source_dir) + 1:-len(".schema.json")]
                    target_path_schema = os.path.join(target_dir, "jsonschema", file_name+".schema.json")
                    target_path_html = os.path.join(target_dir, "html", file_name+".html")
                    with open(schema_path, "r") as schema_file:
                        schema = json.load(schema_file)
                    processed_schema = self._process_schema(source_dir, schema_path, version_number, schema)
                    if processed_schema:
                        self._generate_jsonschema(processed_schema, target_path_schema)
                        self._generate_html(version_number, processed_schema, target_path_html)


if __name__ == '__main__':
    Generator().generate()
