from kuksa_client.grpc import VSSClient
# from piracer.vehicles import PiRacerStandard, PiRacerPro
import time

# piracer = PiRacerPro()
# piracer = PiRacerStandard()

while(1):
    # Assuming the kuksa_client library provides a context manager for VSSClient
    with VSSClient('10.222.31.150', 55555) as client:
        # Subscribe to the vehicle identity paths
        for updates in client.subscribe_current_values([
            'Vehicle.Speed',
            'Vehicle.Chassis.SteeringWheel.Angle',
        ]):
            # Process the received updates
            speed = updates['Vehicle.Speed'].value
            angle = updates['Vehicle.Chassis.SteeringWheel.Angle'].value

            # Print the received updates
            print(f"Received updated Model: {speed}")
            print(f"Received updated Model: {angle}")

    # piracer.set_throttle_percent(speed)
    # piracer.set_steering_percent(angle)
    time.sleep(0.1)

print("Finished. Exiting the subscriber script.")
