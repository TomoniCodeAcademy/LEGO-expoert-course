#
# Run around only within the field  w/ random walk
#

from spike import MotorPair
from spike import ColorSensor
import random
import time

motor_pair = MotorPair('A','B')
color_sensor = ColorSensor('C')

FIELD_COLORS=('blue', 'cyan')

#
#  function:  check inside field or not
#  return value:  True ....  inside field
#                 False .... not inside field
#
def check_inside_field():
    color = color_sensor.get_color()
    #print(color)
    if color in FIELD_COLORS:
        return True
    else:
        return False

counter = 0
speed = 0
steering = 0
while True:
    if check_inside_field():
        print('inside', counter)
        if counter == 0:
            counter = 10
            # random move
            steering = random.randint(-80,80)
            speed = random.randint(5,60)
            print(steering, speed)
            motor_pair.start(speed=speed,steering=steering)
        else:
            counter -= 1
        #time.sleep(1)
    else:
        print('outside!!')
        counter = 0
        # go back    
        print('back and turn')
        motor_pair.move(amount=180, unit='degrees', steering=0, speed=-40)
        motor_pair.move(amount=90, unit='degrees', steering=100, speed=30)
