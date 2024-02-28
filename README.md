# Multi-Agent LLM for Better EV Charge Experience

## About
How far can LLM change your life? How can reverage Decentralized Multi-Agent system?
This project can liberate you from the stress of limited electric vehicle charger! Using LLM and charging station agent, you can make reservation. Futhermore, upon new request of reservation, fully charged vehicles automatically move to a regular parking lot (no charger), allowing new car to charge.
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

## Scenario

1. Vehicle A's user asks DeltaV, "Can I charge in the parking lot?"

2. DeltaV evaluates the spot through its service and determines:

    * The spot is empty.
    * There is a car in the spot, but it has not finished charging.
    * There is a car in the spot, and it is fully charged.

3. Since the charging station has an available spot, DeltaV reserves the spot and confirms the reservation with Vehicle A's user.



https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/f6c5da9d-27ff-4e7c-87c9-11ef7f22278d


4. This time, Vehicle B's user asks DeltaV.
5. Unfortunately, Vehicle A has not finished charging yet. DeltaV informs Vehicle B's user that a reservation cannot be made.

https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/b3538e7b-73af-4247-8996-00605d005b42



6. After some time, Vehicle B's user asks DeltaV again, "Is there a spot available now?"
7. Despite Vehicle A still being at the charging station, DeltaV reserves a spot for Vehicle B's user. How is this possible?
8. The Charging Station knows that Vehicle A has completed charging and requests Vehicle A's agent to move the car to a regular parking area.



https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/2bb246cc-8da1-42ac-b111-df55440d4858


## Future Plan
1. Integration of DeltaV with Voice Recognition
By integrating voice recognition with DeltaV, drivers can communicate with DeltaV through speech while driving to hear about reservations, parking status, and more. Additionally, from the comfort of their home, they can receive updates about their car's status through DeltaV.

2. Vehicle Summoning System

3. Real Testing within a Limited Space
