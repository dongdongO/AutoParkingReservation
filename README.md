# Multi-Agent LLM for Better EV Charge Experience :건전지:

## About
How far can LLM change your life? How can reverage Decentralized Multi-Agent system?
This project can liberate you from the stress of limited electric vehicle charger! Using LLM and charging station agent, you can make reservation. Futhermore, upon new request of reservation, fully charged vehicles automatically move to a regular parking lot (no charger), allowing new car to charge.
This enables Businesses to efficiently manage a small amount of charger to satisfy a large number of users, and Users to enjoy freedom before and after charging.

## Architecture
![Sturcture drawio](https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97211801/c1989442-4d75-46c4-9c69-880f1068c9ab)

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

## Scenario
1. Vehicle A 유저가 deltaV에 물어봅니다. 나 주차장에서 충전 할 수 있어?
2. deltaV가 service를 통해 해당 자리에 대한 판단을 합니다
    * 자리가 비어있다
    * 자리에 차가 있지만 해당 차는 충전이 끝나지 않은 상태이다
    * 자리에 차가 있고 해당 차는 풀충전 상태이다
3. 현재는 충전소에 자리가 비어있기 때문에 deltaV가 자리를 예약해주고 Vehicle A의 유저에게 예약 확인을 해줍니다.

<img src=/demo/scenario1.gif alt="scenario1" width="80%" height="80%"/>

4. 이번에는 Vehicle B 유저가 deltaV에 물어봅니다.
5. 아쉽게도 Vehicle A의 충전이 끝나지 않았네요. deltaV는 Vehicle B유저에게 예약할 수 없다고 합니다.

https://github.com/Bosch-ConnectedExperience-2024/MEMINE/assets/97011426/b3538e7b-73af-4247-8996-00605d005b42


6. 시간이 지난후 Vehicle B 유저가 다시 deltaV에 물어봅니다.
7. 


## Future Plan
1. DeltaV를 통한 차량 -> 음섣인식 + 기능
3. 자동적으로 차량이 내앞에
4. 한정된 공간에서 실제 테스트 / 배포
