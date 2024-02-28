from kuksa_client.grpc import VSSClient
# from jetracer.nvidia_racecar import NvidiaRacecar
import time

# car = NvidiaRacecar() 

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

    car.throttle = speed
    car.steering = angle
    time.sleep(0.1)

print("Finished. Exiting the subscriber script.")
