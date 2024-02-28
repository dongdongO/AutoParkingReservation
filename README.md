# Multi-Agent LLM for Better EV Charge Experience

## TEAM MEMINE
<div align="center">
    <img src="https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/73748884/5eaf2860-fa9f-4a8a-b898-83247a6849ba" width="300" height="300">
</div>

## About
  
How far can LLM change your life? How can reverage Decentralized Multi-Agent system?
This project can liberate you from the stress of limited electric vehicle charger! Using LLM and charging station agent, you can make reservation like any other LLM does. Futhermore, upon new request of reservation, fully charged vehicles automatically move to a regular parking lot (no charger), allowing new car to charge.
This enables Businesses to efficiently manage a small amount of charger to satisfy a large number of users, and Users to enjoy freedom before and after charging.

## Architecture
![Structure drawio](https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97211801/3bf92957-0129-49ca-89bb-4fc700a4988d)

## Keyconcepts
### **DeltaV(LLM)**
  
User can inquire DeltaV as a friend, "Can I park in the parking lot, bro?”. No worries! 
As an LLM model, DeltaV accepts any sentence! 
Even if a fully charged vehicle occupies the charging area, DeltaV informs the user that charging is still possible. 
How this could be possible?

### **Agent**

If some car want to park, then parked car in charger can transmit and receive data as “agent”. Upon receiving information from DeltaV to move the fully charged vehicle, the charger “agent” communicates with the fully charged vehicle to move to regular parking lot. Those uAgents enables fully decentralized structure.

### **Kuksa**

When developing autonomous parking algorithms, there's no need to worry about how to control the vehicle's actuators. 
Just publish to kuksa according to the types defined in COVESA's VSS!

## Demo (How to Follow)

### Setup "Vehicle A" and "Vehicle B" Agents
1. Install uAgent dependency.
2-a. Run agent/local/simulVehicle.py code for visualization with Matplotlib
2-b. Or run agent/local/VehicleA.py and agent/local/VehicleB.py in each JetRacer
3. If then Address will pop up. Remember This!
4. Now, Vehicle Agent is running on your local system.
   
### Setup "Charging Station" Service
1. Go to agentverse's My Agents tab.
2. Register New Agent named "Charger"
3. Copy agent/local/charger.py code and Paste to agent.py in your "Charger" agent
4. Change VEHICLE_AGENT_A and VEHICLE_AGENT_B to Proper Address
5. Reset Agent's Storage to { "charged": false, "occupied": false }
6. Run Your "Charger" Agent, now your Charger Agent is running on Cloud
7. Go to Services tab
8. Register new service group and Make new Service named "Charging Station" with "Charger" agent
   
### Play with DeltaV
1. Go to DeltaV and change to advanced mode
2. Select your service group
3. Ask about Charger and Enjoy!

## Senario

1. Vehicle A's user asks DeltaV, "Can I charge in the parking lot?"

2. DeltaV evaluates the charging spot through its service and determines:

    * The charging spot is empty.
    * There is a car in the charging spot, but it has not finished charging.
    * There is a car in the charging spot, and it is fully charged.

3. Since the charging station has an available spot, DeltaV reserves the spot and confirms the reservation with Vehicle A's user.


https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/7837402b-16ae-4692-93db-ee980c212adf


4. This time, Vehicle B's user asks DeltaV.
5. Unfortunately, Vehicle A has not finished charging yet. DeltaV informs Vehicle B's user that a reservation cannot be made.


https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/0bcf0b21-6fdc-41e2-9c17-c44507e574f8


6. After some time, Vehicle B's user asks DeltaV again, "Is there a charging spot available now?"
7. Despite Vehicle A still being at the charging station, DeltaV reserves a spot for Vehicle B's user. How is this possible?
8. The Charging Station knows that Vehicle A has completed charging and requests Vehicle A's agent to move the car to a other parking area.


https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/d11acff6-cd38-46cc-b510-b3a60f2ac8db



## Future Plan
1. **Integration of DeltaV with Voice Recognition**

    By integrating voice recognition with DeltaV, drivers can communicate with DeltaV through speech while driving to hear about reservations, parking status, and more. Additionally, from the comfort of their home, they can receive updates about their car's status through DeltaV.

2. **Vehicle Summoning System**

    Just as a vehicle that has completed charging can be moved to a regular parking area, DeltaV can also pre-position cars in anticipation of people returning to the parking lot after completing their errands.

3. **Real Testing**

    For testing, an environment is set up on JetRacer, followed by testing and deploying the algorithm.
