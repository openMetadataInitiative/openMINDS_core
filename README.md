# HBP-MINDS
MINDS (Minimum Information for Neuroscience Data Sets) is an ontology-based metadata standard for neuroscience consisting of set of basic information blocks that can be used to describe the origin, context, content, and physical location of individual data in a modular fashion. This repository keeps track of the MINDS schema development for the correspondingly implemented information blocks.

The MINDS schemas capture the following:
* relation of small sets of metadata by grouping them into information blocks (e.g., a SUBJECT metadata block)
* standardized graph relations between information blocks
* standardized keys for requested metadata values including their definition
* relations between metadata across and beyond information blocks by linking to terminologies or an ontologies
* standardization of metadata values by supporting the usage of terminologies or ontologies

## Background of the HBP-MINDS development
MINDS is developed by the curation team of the Neuroinformatics Platform (NIP) of the Human Brain Project (HBP) as part of the effort to build a unique data sharing platform that provides access to a range of heterogeneous neuroscience data. This means that MINDS is applicable for describing and registering data from different modalities including imaging, electrophysiology, informatics, and -omics into a unified database, the HBP Knowledge Graph (KG). As a metadata standard, MINDS is flexible enough to capture experiment-specific aspects, yet strict enough to guarantee comparability across experimental data, which is crucial to facilitate queries across scales and modalities via the KG. 

## Connection between HBP-MINDS and ontologies
Ensuring compatibility with other community efforts for sharing neuroscience data, metadata of the MINDS information blocks are soft-linked to existing neuroscience ontologies: Anticipating that available ontologies might not yet be complete, new metadata entries are not strictly forced to follow the terminology of an ontology. In fact, metadata entries that do not match an ontology term are triggers for complementing or optimizing existing ontologies.

## Past and current HBP-MINDS versions
Although the term "MINDS" was introduced quite early in the HBP, it's implementation underwent some rather drastic changes during the developmental and application stages in the last years. Please find in the following for each released version an outline of the corresponding architecture of MINDS and a list of changes in the metadata structure to the former version. Please note, that the KG system only supports the latest released 

### HBP-MINDS version 0.1 (released: )
The HBP-MINDS version 0.1 development started shortly after the ramp-up phase (RUP) of the HBP. At that point in time, the KG was not fully implemented as the HBP database, and a corresponding KG editor was not yet in place. Integration of MINDS metadata was conducted via an input mask (Data Workbench) for a relational database that was temporarily in place before the first HBP KG release. 

### HBP-MINDS version 0.2 (released: Oct 2018)
The HBP-MINDS version 0.2 unified the metadata schemas across species and increased the modularity of the MINDS architecture. 
#### HBP-MINDS version 0.2.1 (released: Feb 2019)
The HBP-MINDS version 0.2.1 only corrected the naming convention of a few metadata blocks and included a revised edition of the metadata key definitions.

### HBP-MINDS version 0.3 (in development)
The HBP-MINDS version 0.3 is currently in development and will include changes in the block structure to further increase the modularity and with that the descriptive capablitlies of the metadata schema.

## License
HBP-MINDS is developed under the CC BY 4.0 license. 
