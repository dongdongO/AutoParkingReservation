# Decentralized Mobility Agents


![](assets/Mendix-Primary-Logo-RGB-Blue-h60.png)

- [About](#about)
    - [Hackcoaches](#hack-coaches)
- [What we offer](#tech-stack-overview)
- [Example use-case](#an-example-use-case)
- [Getting Started](#getting-started)
    - [Pre-requisites](#pre-requisites)
    - [Hackathon setup](#hackathon-setup-configuration)

## About
In this challenge, we, as Mobility Providers, are dedicated to creating the ultimate travel experience for our customers. Our goal is to engineer vehicles that seamlessly navigate the complexities of ever-changing situations, ensuring that passengers feel at ease and thoroughly enjoy their journey. We aim to innovate and push the boundaries of what's possible, making every trip not just a journey, but an experience to remember

## Hack Coaches
### Bosch
- Indrasen Raghupatruni
- Himajit Aithal
- Pavel Simo
### Fetch.ai
- Maria Minaricova 
- Florian Wilde
- Edward FitzGerald

## Tech Stack overview

Software stack comprises of [playground.digital.auto
](https://digitalauto.netlify.app), Bosch SSI & IBM Decentralized infrastructure along with Fetch.ai [Agentverse](https://fetch.ai/docs/concepts/agent-services/agentverse-intro) and [DeltaV](https://fetch.ai/docs/concepts/ai-engine/deltav) platforms. API are enabled by the SDV software stack, mainly [Eclipse.LEDA](https://github.com/eclipse-leda) and [Eclipse.Kuksa](https://github.com/eclipse/kuksa.val) and ROS/[DDS](https://github.com/eclipse-cyclonedds/cyclonedds) to enable vehicle applications. SSI software stack enables decentralized identity (DID) and Fetch.ai agents enable discoverable services enhanced by natural language based communication medium. 

![SW stack](figures/SW_Stack.png?raw=true "SW stack")


Here is the detailed stack of the infrastructure and the hardware devices 

![Tech stack](figures/Tech_Stack.png?raw=true "Tech stack")

## An example use-case

Detect driver's range anxiety through car's AI, engage Voice/Chat assist, obtain goal to locate and book charging station, process with context aware agent, activate search and booking service, notify driver of scheduled slot, authenticate at charging station, handle transaction autonomously, notify driver, continue journey with content driver. 

Users can simulate the scenario in [Metaverse](https://blog.bosch-digital.com/metaverse-a-place-for-education-and-training/) or use the hardware with provided [TechStack](#tech-stack-overview)

## Getting started

### Pre-requisites
Participants are expected to have the following tools installed in their laptop
- [tailscale](https://tailscale.com) (to access the hardware) -> login with github account
- Docker / [colima](https://github.com/abiosoft/colima) (to execute docker in macOS)
- Python (v3.10+ recommended)
- Fetch.ai [Agentverse](https://agentverse.ai/) account -> login with gmail account
- Fetch.ai [DeltaV](https://deltav.agentverse.ai/) -> login with gmail account


### Hackathon setup configuration
Here are configuration details for the infrastrucure and hardware

### Hardware
- [JetRacer](/jetracer/jetracer-settings.md)
- [Mock-charger](/mock-charger/infra-settings.md)
- [virtual HW](/virtual/getting-started-virtualHW.md)
### Software
- [SSI stack](/ssi/ssi-settings.md)
- [Kuksa.val](https://github.com/eclipse/kuksa.val)
    - Sample code to run kuksa client is available in [JetRacer document](/jetracer/jetracer-settings.md) and [mock-charger document](/mock-charger/infra-settings.md)
- [DDS](https://github.com/eclipse-cyclonedds/cyclonedds)
    - Sample code to run DDS publisher and subscriber are available in [JetRacer document](/jetracer/jetracer-settings.md) and [mock-charger document](/mock-charger/infra-settings.md) respectively.
- [metaverse](https://github.com/Bosch-ConnectedExperience-2024/SDV_GettingStarted/blob/WIP.SDVLINK.DOCS/sdv-link-mixed-reality-kit.md)    
- [wallet chat](/resources/Chat%20to%20X.pptx)
- [Fetch.ai Agent Stack](/fetchai/README.md)
### Infrastructure
- [Bosch Infrastructure](/host/bosch-host-settings.md)