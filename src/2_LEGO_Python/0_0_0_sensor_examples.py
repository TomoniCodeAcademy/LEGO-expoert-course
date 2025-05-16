#
#  sensor examples
#

import time

# example force sensor
from spike import ForceSensor
force = ForceSensor('A')
while True:
    newtons = force.get_force_newton()    # get value: 0 - 10
    print(newtons)
    time.sleep(0.5)

# example distance sensor
from spike import DistanceSensor
distance = DistanceSensor('B')
while True:
    print(distance.get_distance_cm(short_range=False))  # value: none, 4-200
    time.sleep(0.5)

#example color sensor
from spike import ColorSensor
color = ColorSensor('C')
while True:
    print(color.get_reflected_light())# value: 0-99
    time.sleep(0.5)

# example servo as sensor
from spike import Motor
motor = Motor('D')
motor.set_degrees_counted(0)
while True:
    print('pos', motor.get_position())     # value: 0-360
    print('count', motor.get_degrees_counted())  # value: -oo - 0 - + oo
    time.sleep(0.5)
  
