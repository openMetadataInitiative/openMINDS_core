# openMINDS
Welcome **openMINDS**, the open Metadata Initiative for Neuroscience Data Structures powered by the [HBP](https://www.humanbrainproject.eu/en/) (Human Brain Project) and [EBRAINS](https://ebrains.eu/) (European Brain ReseArch INfraStructure).

openMINDS is a collection of ontology-based metadata schemas for neuroscience data structures, developed and maintained by the curation team of the HBP Neuroinformatics Platform (NIP). Currently supported data structures are data generated in experimental laboratories (across all neuroscience modalities) as well as the code of computational models and software. 

The schemas are the architectural building blocks of the Knowledge Graph (KG) database, a unique data sharing framework powered by HBP and hosted on EBRAINS. As a metadata standard, openMINDS is flexible enough to capture the specific aspects of the data structures, yet strict enough to guarantee comparability across them to facilitate queries via the [KG Search UI](https://kg.ebrains.eu/search). Moreover, wherever it is applicable, openMINDS metadata (properties and values) are linked to neuroscience terminologies or ontologies that are also used outside of the KG database. 

The openMINDS schemas can be used to describe the origin, context, content, and physical location of individual or entire sets of data files in a modular fashion. In general, each schema captures ...
* ... the information context of the contained metadata (e.g, subject), 
* ... a set of required or optional metadata (e.g., for subject: species, biological sex, etc.), 
* ... the expected value type of each metadata entry (e.g., reference to another schema, date, etc.), 
* ... and in some cases even a drop-down list of possible values for a specific metadata entry.

All openMINDS schemas are defined in JSON-Schema and can be serialized in JSON-LD. The latter can also be directly digested as machine-readable data descriptions into the database of the KG. More information about the technical implementation of the openMINDS schemas and their usage can be found in [Implementation & Usage](https://github.com/HumanBrainProject/openMINDS/wiki/Implementation-&-Usage).

Using openMINDS metadata schemas for describing data will increase their findability and interoperability according to the FAIR guiding principles for scientific data management and stewardship ([Wilkinson et al. 2016](https://doi.org/10.1038/sdata.2016.18)).

### History Recap
Within the HBP, the first basic metadata schemas were called Minimal Information for Neuroscience Data Set (MINDS) and introduced by [Hill et al. (2016)](https://doi.org/10.1038/nrn.2016.134). Since then, the implementation of the schemas underwent some rather drastic changes. Please find in the following a short outline for each version of the openMINDS metadata schemas.

#### v1: MINDS
[released: Mar 2017] As mentioned above, the first version was called MINDS. It's development started shortly after the ramp-up phase of the HBP. At that time, the integration of MINDS metadata was conducted via an input mask (Data Workbench) for a relational database that was temporarily in place before the first release of the KG framework towards the late SGA-1 phase of the HBP. This first KG release comprised a translation of the previous relational database to a graph database, and the provision of a new metadata input mask, the KG editor. Although MINDS was modified and extended over time, until now, the schemas are used as building blocks of the KG database in combination with the model schemas defined in v2: uniMINDS. 

#### v2: uniMINDS 
[partial release: Okt 2018] The second version, called uniMINDS, was never fully released, but rather functioned as a test environment for fully utilizing the power of the KG graph database. In comparison to MINDS, the modularity of the uniMINDS schemas was increased to enabled individual describtions of subjects, tissue samples and files. Furthermore, uniMINDS included a metadata schema for computational models. Until now, the model schema is the only released part of uniMINDS.

#### v3: openMINDS
[in development] The third version of the HBP basic metadata schemas was renamed to openMINDS. Based on experiences collected from the v2: uniMINDS environment, openMINDS will comprise renewed schemas that best integrate with ontologies and other metadata schemas developments within and outside of HBP and EBRAINS. Furthermore, openMINDS will be able to handle information of software, and time-dependent measurements performed on subjects or tissue samples. It's release is planned for the early SGA-3 phase of the HBP.

## License
This work is licensed under a Creative Commons Attribution 4.0 International License.
