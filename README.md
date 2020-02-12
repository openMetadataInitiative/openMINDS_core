# openMINDS
openMINDS (open Metadata Initiative for Neuroscience Data Structures) is an ontology-based metadata standard for neuroscience. It is developed by the curation team of the Neuroinformatics Platform (NIP) of the Human Brain Project (HBP) as part of the effort to build a unique data sharing framework, called the Knowledge Graph (KG), within the HBP powered European Brain ReseArch InfraStructure, short EBRAINS. 

openMINDS is applicable for describing and registering data from different modalities including imaging, electrophysiology, informatics, and -omics into unified graph databases, such as the KG database hosted by EBRAINS. As a metadata standard, openMINDS is flexible enough to capture specific aspects of the data, yet strict enough to guarantee comparability across them. 

To this end, openMINDS consists of a set of core information blocks (schemas) that can be used to describe the origin, context, content, and physical location of individual or entire sets of data files in a modular fashion.

In short, openMINDS schemas capture the following:
  + type of each schema
  + properties of each schema
  + relations between schemas
  + type-validation of certain values within the schemas
  + potential value suggestions extracted from existing terminologies (openMINDS-options) and/or ontologies
  
All openMINDS schemas are defined in JSON-Schema and can be serialized in JSON-LD. The latter can also be directly digested as machine-readable data descriptions into the database of the EBRAINS KG which will increase the findability of the corresponding data.

## Connecting MINDS to the world.
For ensuring compatibility with other community efforts for sharing neuroscience data, openMINDS metadata are linked to existing neuroscience terminologies or ontologies that were registered in the EBRAINS KG framework. Keeping in mind, though, that most standardization efforts are not completed or dynamicly evolve, openMINDS metadata entries (values) are not forced to strictly follow a registered terminology or ontology, but can be instead defined by the individual user. In fact, metadata entries that cannot be linked to an available terminology or ontology term within the EBRAINS KG, will trigger the completion or optimization of the correspondingly registered terminologies or ontologies.

## openMINDS history
Within the HBP, the first basic metadata schemas were called Minimal Information for Neuroscience Data Set (MINDS) and introduced by [Hill et al. (2016)](https://doi.org/10.1038/nrn.2016.134). Since then, the implementation of the MINDS schemas underwent some rather drastic changes during the developmental and application stages within the HBP. Please find in the following for each released version an outline of the corresponding architecture of the HBP basic metadata schemas. Please note, that the EBRAINS KG framework only supports the latest released version.

### version 1.0
[released: Mar 2017] The first version of the HBP basic metadata schemas was called MINDS v1.0. It's development started shortly after the ramp-up phase (RUP) of the HBP. Integration of MINDS metadata was conducted via an input mask (Data Workbench) for a relational database that was temporarily in place before the first release of the KG framework towards the late SGA-1 phase of the HBP. This first KG release comprised a translation of the previous relational database to a graph database, and the provision of a new metadata input mask, the KG editor. MINDS v1.0 consisted of the following six core schemas: 
  + ***PLA Component*** 
  + ***Dataset***
  + ***Activity***
  + ***Specimen Group***
  + ***Subject***
  + ***Sample***

Although MINDS v1.0 was modified and extended over time, the core schemas were used as building blocks of the KG database until now.

### version 2.0 
[restricted release: Okt 2018] The second version of the HBP basic metadata schemas (MINDS v2.0) was never fully released, but functioned as a test environment for fully utilizing the power of the KG graph database. In comparison to MINDS v1.0, the modularity of the MINDS v2.0 schemas was increased to enabled individual describtions of subjects, tissue samples or files. Furthermore, MINDS v2.0 included a metadata schema for computational models which was used to integrate corresponding data into the KG framework. The corresponding landing pages were the only released parts of MINDS v2.0 within the KG database. In summary, MINDS v2.0 consisted of the following fifteen core schemas:
  + ***Project*** 
  + ***Person*** 
  + ***ModelRelease*** 
  + ***Dataset*** 
  + ***EthicsApproval*** 
  + ***FundingInformation*** 
  + ***Publication/Source*** 
  + ***HBPcomponent*** 
  + ***SubjectGroup*** 
  + ***Subject*** 
  + ***TissueSample*** 
  + ***FileBundle*** 
  + ***File*** 
  + ***Method/Paradigm*** 
  + ***StudyTarget*** 

### version 3.0
[in development] The third version of the HBP basic metadata schemas was renamed to openMINDS v3.0. Based on experiences collected from the MINDS v2.0 test environment, openMINDS v3.0 will comprise renewed schemas that best integrate with ontologies and other metadata schemas developments (cf. SANDS and NAR) within HBP. Furthermore, openMINDS v3.0 will be able to handle information of software, and time-dependent measurements performed on subjects or tissue samples. In summary, openMINDS v3.0 will consist of the following seventeen core schemas:
  + ***Project*** 
  + ***Person***
  + ***Model*** 
  + ***Dataset*** 
  + ***Software***
  + ***Subject***
  + ***TissueSample***
  + ***MeasurementsSubject***
  + ***MeasurementsTissueSample***
  + ***File***
  + ***AnatomicalAttribution***
  + ***Performance***
  + ***Protocol***
  + ***Technique*** 
  + ***Task***
  + ***Parameters***
  + ***StudyTarget***

## License
This work is licensed under a Creative Commons Attribution 4.0 International License. 
