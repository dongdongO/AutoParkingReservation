from pydantic import Field
from ai_engine import UAgentResponse, UAgentResponseType

class Charger(Model):
    request: str = Field(description="Ask to select between Status and Reserve.")

# Position.x = 0 -> move to charger
# Position.x = 1 -> move to parking lot
class Position(Model):
    id: str
    x: int

# This is the address of the weather provider agent

VEHICLE_AGENT_A = "agent1q00up4d66s77ywhjkjlzu732y5c4tsv494v22shxljpgtzns4r8jzc87f73"
VEHICLE_AGENT_B = "agent1qgek6awxu0mlc07u4zzpa4fgqtrt4h6yzmfpd684qxkxlk3zss3tg5cppzq"
VEHICLE_AGENT_ADDRESS = {"A" : VEHICLE_AGENT_A, "B" : VEHICLE_AGENT_B}

charging_protocol = Protocol("Charger")
@charging_protocol.on_message(model=Charger, replies={UAgentResponse})
async def response(ctx: Context, sender: str, msg: Charger):
    if msg.request == "Status":
        if ctx.storage.get("occupied"):
            if ctx.storage.get("charged"):
                message = "Charger is Already Occupied, but Charging is finished"
                ctx.storage.set("occupied", True)
                ctx.storage.set("charged", True)
            else:
                message = "Charging Another Vehicle"
                ctx.storage.set("occupied", True)
                ctx.storage.set("charged", False)
        else:
            message = "Charger is Free Now"
            ctx.storage.set("occupied", False)
            ctx.storage.set("charged", False)
    elif msg.request == "Reserve":
        if ctx.storage.get("occupied"):
            if ctx.storage.get("charged"):
                message = "Already occupied, But I will move this car. Reservation Success"
                ctx.storage.set("occupied", True)
                ctx.storage.set("charged", False)
                await ctx.send(VEHICLE_AGENT_ADDRESS["A"], Position(id="A", x=1))
                await ctx.send(VEHICLE_AGENT_ADDRESS["B"], Position(id="B", x=0))
            else:
                message = "Charger is Already Occupied, You need to wait!"
                ctx.storage.set("occupied", True)
                ctx.storage.set("charged", True)
        else:
            message = "Charger is Free Now, Reservation Success"
            ctx.storage.set("occupied", True)
            ctx.storage.set("charged", False)
            await ctx.send(VEHICLE_AGENT_ADDRESS["A"], Position(id="A", x=0))
    else:
        message = "Select Status or Reserved, Retry Please!"

    await ctx.send(
        sender, UAgentResponse(message=message, type=UAgentResponseType.FINAL)
)

agent.include(charging_protocol, publish_manifest=True)
    