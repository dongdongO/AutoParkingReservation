
## Structure
![structure drawio](https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97211801/f26fd6ca-d617-4c8b-80cf-6c7e62ac7b22)

## Charging Station Agent (Cloud)
We use this Decentralized Agent using DeltaV (LLM) 
- Service Name : Charging Station
- Describtion : This is nearest charging station from vehicle
- Storage: { "charged": false, "occupied": false }

## Vehicle A Agent (Local, JetRacer)
- Move vehicle by receiving message from cloud

## Vehicle B Agent (Local, JetRacer)
- Same Algorithm with A
