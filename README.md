# HBP-MINDS
MINDS (Minimum Information for Neuroscience Data Sets) is an ontology-based metadata standard for neuroscience. It is developed by the curation team of the Neuroinformatics Platform (NIP) of the Human Brain Project (HBP) as part of the effort to build a unique data sharing framework that provides access to a broad range of heterogeneous neuroscience data. This means that MINDS is applicable for describing and registering data from different modalities including imaging, electrophysiology, informatics, and -omics into a unified graph database, the HBP Knowledge Graph (KG). As a metadata standard, MINDS is flexible enough to capture experiment-specific aspects, yet strict enough to guarantee comparability across experimental data, which is crucial to facilitate queries across scales and modalities via the KG. 

To this end, MINDS consists of a set of core information blocks that can be used to describe the origin, context, content, and physical location of individual data in a modular fashion. The MINDS schemas are provided in JSON-Schema and capture the following:
  + type of each information block
  + properties of each information blocks
  + relations between information blocks
  + validation of value type
  + link to possible terminologies and ontologies for value suggestions

## Connecting MINDS to the world
For ensuring compatibility with other community efforts for sharing neuroscience data, metadata of the MINDS core information blocks are linked to existing neuroscience terminologies or ontologies that were registered into the KG system. However, new metadata entries are not forced to strictly follow a registered terminology or ontology, because most standardization efforts are not yet completed. In fact, metadata entries used in the HBP KG that do not match a terminology or ontology term, trigger the completion or optimization of existing terminologies or ontologies.

## MINDS history
Although the term "MINDS" was introduced quite early in the HBP, it's implementation underwent some rather drastic changes during the developmental and application stages in the last years. Please find in the following for each released version an outline of the corresponding architecture of MINDS and a list of changes in the metadata structure to the former version. Please note, that the KG system normally only supports the latest released version.

### MINDS version 1.0
[released: Mar 2017] The MINDS v1.0 development started shortly after the ramp-up phase (RUP) of the HBP. However, during the RUP the KG was not yet implemented as the HBP database. Integration of MINDS metadata was conducted via an input mask (Data Workbench) for a relational database that was temporarily in place before the first HBP KG release towards the late SGA-1 phase of the HBP. This first HBP KG release comprised a translation of the previous relational database to a graph database, and the provision of a new metadata input mask, the KG editor. At that time, the MINDS v1.0 consisted of the following six core information blocks: 
  + ***PLA Component*** 
  + ***Dataset***
  + ***Activity***
  + ***Specimen Group***
  + ***Subject***
  + ***Sample***

### HBP-MINDS version 2.0 
[restricted release: Okt 2018] MINDS v2.0 increased the modularity of the block architecture in order to utilize fully the power of HBP KG as graph database. In comparison to MINDS v1.0, MINDS v2.0 allows users to describe methods or paradigms for individual subjects, tissue samples or files. MINDS v2.0 incorporated also the possibility to group individual subjects into different subject groups at the same time which facilitated the metadata registration and connections across datasets that use the same subjects. MINDS v2.0 consists of the following fifteen core information blocks:
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

### HBP-MINDS version 3.0
[in development] MINDS v3.0 improved the modularity of the block architecture in order to simplify the graph structure in the KG, but optimize the handling of versioning and time-dependent information of a subject (e.g., age at time point of measurement). MINDS v3.0 consists of the following thirteen core information blocks:
  + ***Project*** 
  + ***Person*** 
  + ***Model*** 
  + ***Dataset*** 
  + ***EthicsApproval*** 
  + ***FundingInfo*** 
  + ***PublicationOrSource*** 
  + ***Subject(s)***
  + ***TemporalSubjectInfo***
  + ***TissueSample(s)***
  + ***File(s)***
  + ***MethodOrParadigm*** 
  + ***StudyTarget***

## License
All HBP-MINDS versions are developed under the CC BY 4.0 license. 
