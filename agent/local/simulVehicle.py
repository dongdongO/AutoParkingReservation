from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model

import time
import matplotlib.pyplot as plt

# First generate a secure seed phrase (e.g. https://pypi.org/project/mnemonic/)
SEED_PHRASE = "memine/vehicleA"

# Copy the address shown below
print(f"Your agent's address is: {Agent(seed=SEED_PHRASE).address}")
 
# Then go to https://agentverse.ai, register your agent in the Mailroom
# and copy the agent's mailbox key
AGENT_MAILBOX_KEY = "4865408c-b061-4416-bc51-d939f8e29fb5"
 
# Now your agent is ready to join the agentverse!
agent = Agent(
    name="VehicleA",
    # port=8000,
    seed=SEED_PHRASE,
    # endpoint=["http://127.0.0.1:8000/submit"],
    mailbox=f"{AGENT_MAILBOX_KEY}@https://agentverse.ai",
)

fund_agent_if_low(agent.wallet.address())

class Position(Model):
    id: str
    x: int

@agent.on_message(model=Position)
async def position_response(ctx: Context, addr, msg: Position):
    global statusA
    global statusB
    global xA, yA
    global xB, yB
    ctx.logger.info(f"Got Message id : {msg.id}, x : {msg.x}")
    
    moveA = False
    moveB = False
    if msg.id == "A":
        statusA = msg.x
        moveA = True
        if statusA == 2:
            statusB = 1
            moveB = True
        
    while moveA or moveB:
        if statusA == 0:
            pass
        elif statusA == 1:
            # move A to charger
            if xA==40 and yA==70:
                statusA = 0
                moveA = False
            else:
                xA += 1
                yA += 2
        elif statusA == 2:
            # move A to Parking lot and move B to charger
            if xA==80 and yA==90:
                statusA = 0
                moveA = False
            else:
                xA += 2
                yA += 1
                
        if statusB == 0:
                pass
        elif statusB == 1:
            # move B to charger
            if xB==40 and yB==70:
                statusB = 0
                moveB = False
            else:
                xB += 1
                yB += 2
        
        plt.clf()
        plt.plot([0,100,100,0,0], [0,0,100,100,0], color='white')
        x,y,w,h = 35,65,10,10
        plt.plot([x,x+w,x+w,x,x], [y,y,y+h,y+h,y], color='green', linewidth=3)
        plt.text(x+w/2, y+h*1.2, "Charger", fontsize = 20, ha='center', weight='bold')
        x,y,w,h = 75,85,10,10
        plt.plot([x,x+w,x+w,x,x], [y,y,y+h,y+h,y], color='blue', linewidth=3)
        plt.text(x+w/2, y+h*1.2, "Parking Lot", fontsize = 20, ha='center', weight='bold')
        plt.scatter(xA,yA, linewidths=10)
        plt.scatter(xB,yB, linewidths=10)
        plt.pause(0.1)
    # plt.show()
 
if __name__ == "__main__":
    statusA = 0
    statusB = 0
    xA, yA = 10, 10
    xB, yB = 10, 10
    plt.figure(figsize=(10,10))
    plt.plot([0,100,100,0,0], [0,0,100,100,0], color='white')
    x,y,w,h = 35,65,10,10
    plt.plot([x,x+w,x+w,x,x], [y,y,y+h,y+h,y], color='green', linewidth=3)
    plt.text(x+w/2, y+h*1.2, "Charger", fontsize = 20, ha='center', weight='bold')
    x,y,w,h = 75,85,10,10
    plt.plot([x,x+w,x+w,x,x], [y,y,y+h,y+h,y], color='blue', linewidth=3)
    plt.text(x+w/2, y+h*1.2, "Parking Lot", fontsize = 20, ha='center', weight='bold')
    plt.scatter(xA,yA, linewidths=10)
    plt.scatter(xB,yB, linewidths=10)
    plt.pause(0.1)
    agent.run()
    