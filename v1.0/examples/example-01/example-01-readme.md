## Example-01 README
The example-01 gives a short impression on how an openMINDS metadata collection would look like for an invented experimental study. The example does not connect to any data, it was purely intended for explaining the structure of a v1: MINDS conform metadata collection.

**Background story:** The invented experimental study was performed by three imaginary researchers, Jane Jupitor, Paul Crenshaw, and Beatrice Andrews. Beatrice Andrews is the principal investigator that led the study and who is responsible for maintaining the correspondingly produced data. The study was performed on four pseudonymised linving human beings (two males, two females) of various age. Data were obtained for each subject under resting state condition once using electroencephalography (EEG) and once using function magnetic resonance imaging (fMRI). The study was ethically approved by an imaginary ethics committee.

Here a structural overview of the corresponding example-01 metadata collection:  
> ....**minds/**  
> ........**core/**  
> ............**activity/**  
> ................**v1.0.0/**  
> ....................**activity-01.json**  
> ....................**activity-02.json**  
> ............**agecategory/**  
> ................**v1.0.0/**  
> ....................**adult.json**  
> ....................**juvenile.json**  
> ............**dataset/**  
> ................**v1.0.0/**  
> ....................**dataset-01.json**  
> ............**person/**  
> ................**v1.0.0/**  
> ....................**person-01.json**  
> ....................**person-02.json**  
> ....................**person-03.json**  
> ............**preparation/**  
> ................**v1.0.0/**  
> ....................**in-vivo.json**  
> ............**sex/**  
> ................**v1.0.0/**  
> ....................**male.json**  
> ....................**female.json**  
> ............**species/**  
> ................**v1.0.0/**  
> ....................**homo-sapiens.json**  
> ............**specimengroup/**  
> ................**v1.0.0/**  
> ....................**specimengroup-01.json**  
> ........**ethics/**  
> ............**approval/**  
> ................**v1.0.0/**  
> ....................**approval-01.json**  
> ............**authority/**  
> ................**v1.0.0/**  
> ....................**authority-01.json**  
> ........**experiment/**  
> ............**method/**  
> ................**v1.0.0/**  
> ....................**method-01.json**  
> ....................**method-02.json**  
> ....................**method-03.json**  
> ............**subject/**  
> ................**v1.0.0/**  
> ....................**subject-01.json**  
> ....................**subject-02.json**  
> ....................**subject-03.json**  
> ....................**subject-04.json**  
