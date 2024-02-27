from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint

import time

# Example VIN and other identity attributes
Speed = 10
Angle = 20

for i in range(10):
    with VSSClient('10.222.31.150', 55555) as client:
        # Set VIN, Make, and Model as an example. Adjust paths as per your VSS schema.
        client.set_current_values({
            'Vehicle.Speed': Datapoint(Speed),
            'Vehicle.Chassis.SteeringWheel.Angle': Datapoint(Angle),
        })
        print(f"Published Vehicle Identity: Speed={Speed}, Angle={Angle}")
    Speed += 10
    Angle += 5
    time.sleep(1)

print("Finished.")
