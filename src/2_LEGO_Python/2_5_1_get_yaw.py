import time
from spike import PrimeHub

hub = PrimeHub()

# set yaw angle to 0
hub.motion_sensor.reset_yaw_angle()

while True:
    angle = hub.motion_sensor.get_yaw_angle()
    print('Angle:', angle)
    time.sleep(1)


# hub.motion_sensor.get_pitch_angle() 
# hub.motion_sensor.get_roll_angle() 