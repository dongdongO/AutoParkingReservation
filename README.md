
## Structure
![structure drawio](https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97211801/6b97d6ad-4de1-432f-95d2-e64962c18074)


## Charging Station Agent (Cloud)
We use this Decentralized Agent using DeltaV (LLM) 
- Service Name : Charging Station
- Describtion : This is nearest charging station from vehicle
- Storage: { "charged": false, "occupied": false }

## Vehicle A Agent (Local, JetRacer)
- Move vehicle by receiving message from cloud

## Vehicle B Agent (Local, JetRacer)
- Same Algorithm with A
