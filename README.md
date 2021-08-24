<a href="https://github.com/HumanBrainProject/openMINDS_core/blob/v3/img/openMINDS_core_logo.png">
    <img src="https://github.com/HumanBrainProject/openMINDS_core/blob/v3/img/light_openMINDS-core-logo.png" alt="openMINDS core logo" title="openMINDS core" align="right" height="70" />
</a>

# openMINDS_core

The **openMINDS_core** repository is part of the **open** **M**etadata **I**nitiative for **N**euroscience **D**ata Structures (**openMINDS**). It contains 
schemas used to describe the general origin, location and content of neuroscience research products. The openMINDS_core schemas cover metadata for the basic integration of research products into the EBRAINS Knowledge Graph.

The major versions are developed and maintained in different version-branches. **Each version can be accessed by checking out the corresponding version-branch.** You are currently on **version-branch v3**. Note: the default branch is always the latest version-branch in use within the EBRAINS Knowledge Graph. 

For application and technical details please go to the [central openMINDS repository](https://github.com/HumanBrainProject/openMINDS) or the [openMINDS Collab](https://wiki.ebrains.eu/bin/view/Collabs/openminds/).

## schemas
In the **schemas** directory, all openMINDS_core schemas (v3) are defined in the openMINDS syntax (`*.schema.tpl.json`). Details about the openMINDS syntax can be found [here](https://wiki.ebrains.eu/bin/view/Collabs/openminds/Documentation/Implementation%20details/#HTheopenMINDSsyntax). For convenience, related openMINDS_core schemas are grouped into subdirectories. To ensure a central access point for all openMINDS schemas across all versions and metadata models, each change in the schemas will lead to a new build of the central openMINDS repository.

## instances
In the **instances** directory, it is possible to store **controlled instances** (as JSONLDs) for selected openMINDS_core schemas (v3). The subdirectory of **instances** should resemble the **schemas** directory with the schema type as an additional subdirectory. The controlled instances are used within the EBRAINS Knowledge Graph to increase data integration.
 
## tests
In the **tests** directory you can find JSON-LDs designed to test the validation behaviour of each schema. The subdirectory of **tests** should resemble the **schemas** directory with the schema type as an additional subdirectory. Each JSON-LD follows the naming convention `{schema_name}-{custom_test_name}.jsonld`. For test cases supposed to fail the validation, the suffix **`-nok`** should be attached (`{schema_name}-{custom_test_name}-nok.jsonld`). The tests are validated every time a change is introduced and therefore are ensuring the correct behavior of the schemas.

## examples
In **examples** you will find several possible serializations of the openMINDS_core metadata model. The scope of each example is described in it's README. The correspondingly generated JSON-LDs may be further structured (e.g., grouped according to the schema they are validated against).

## How to contribute
Please check our [contribution document](./CONTRIBUTING.md).

## License
This work is licensed under the MIT License.

**Logo:** The openMINDS logo was created by U. Schlegel, based on an original sketch by C. Hagen Blixhavn and feedback by L. Zehl.
