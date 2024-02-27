from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model

# First generate a secure seed phrase (e.g. https://pypi.org/project/mnemonic/)
SEED_PHRASE = "memine/vehicleB"

# Copy the address shown below
print(f"Your agent's address is: {Agent(seed=SEED_PHRASE).address}")
 
# Then go to https://agentverse.ai, register your agent in the Mailroom
# and copy the agent's mailbox key
AGENT_MAILBOX_KEY = "6254fdc2-9385-4e3c-8385-dfdf5aa24e1e"
 
# Now your agent is ready to join the agentverse!
agent = Agent(
    name="VehicleB",
    # port=8001,
    seed=SEED_PHRASE,
    # endpoint=["http://127.0.0.1:8001/submit"],
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