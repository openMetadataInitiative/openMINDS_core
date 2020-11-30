# openMINDS_core

The openMINDS_core repository is part of the open Metadata Initiative for Neuroscience Data Structures (openMINDS). It contains the 
schema-templates used for registering neuroscience research products into the EBRAINS Knowledge Graph.

**The different versions can be accessed by checking out their version-branch**

For more information on openMINDS in general and the processing pipelines for the schema-templates please go to the main repository: https://github.com/HumanBrainProject/openMINDS

## schemas
The core v3 schemas are JSON-schema inspired schema-templates with a few custom template-properties (prefixed with `"_"`) which allow us to simplify their readability and increase their reusability.

## tests
In **tests** you can find JSON-LDs designed to test the validation behaviour of each schema. These test JSON-LDs are grouped according to the used core schema categories (actors, data, miscellaneous, products, and research). Each JSON-LD follows the naming convention `{schema_name}-{custom_test_name}.jsonld`. For test cases supposed to fail the validation, the suffix **`-nok`** should be attached (`{schema_name}-{custom_test_name}-nok.jsonld`). The tests are validated every time a change is introduced and therefore are ensuring the correct behavior of the schemas.

## examples
In **examples** you will find several possible serializations of the openMINDS_core metadata model. The scope of each example is described in it's README. The correspondingly generated JSON-LDs may be further structured (e.g., grouped according to the schema they are validated against).

## How to contribute
Please check our [contribution document](./CONTRIBUTING.md).

## License
This work is licensed under the MIT License.
