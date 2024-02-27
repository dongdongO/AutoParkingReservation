from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model

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
    ctx.logger.info(f"Got Message id : {msg.id}, x : {msg.x}")
 
if __name__ == "__main__":
    agent.run()