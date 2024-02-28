# Decentralized Mobility Agents
## About
How far can LLM change your life? 
This project can liberate you from the stress of limited electric vehicle infrastructure! 
Upon user request, fully charged vehicles automatically move to a regular parking area, allowing users to occupy the charging spot. 
This enables businesses to efficiently manage a small infrastructure to satisfy a large number of users, and users can enjoy freedom before and after charging.

## Architecture
![structure drawio](https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97211801/6b97d6ad-4de1-432f-95d2-e64962c18074)

## Keyconcepts
### **deltaV(LLM)**
  
User can inquire deltaV as a friend, "Can I park in the parking lot, bro?”. No worries! 
As an LLM model, deltaV accepts any sentence! 
Even if a fully charged vehicle occupies the charging area, deltaV informs the user that charging is still possible. 
How this could be possible?

### **Agent**
  
Both the vehicle attempting to park and the one in charger can transmit and receive data as “agent”. 
Upon receiving information from deltaV to move the fully charged vehicle, the central parking manager communicates with the fully charged vehicle's agent to move to regular parking lot.
This allows for the completion of a fully decentralized structure.

### **Kuksa**

When developing autonomous parking algorithms, there's no need to worry about how to control the vehicle's actuators. 
Just publish to kuksa according to the types defined in COVESA's VSS!

## Demo
