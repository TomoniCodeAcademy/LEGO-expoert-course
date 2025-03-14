#
# go straight or turn only within the field
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

while True:
    if check_inside_field():
        # random move
        move = ('straight', 'turn')[random.randint(0, 1)]
        print(move)
        if move == 'straight':
           # go straight
            motor_pair.start(speed=60,steering=0)
        elif move == 'turn':
            motor_pair.start(speed=60,steering=20)
        time.sleep(1)
    else:
        print('outside!!')
        # go back and turn    
        motor_pair.move(amount=90, unit='degrees', steering=0, speed=-40)
        motor_pair.move(amount=90, unit='degrees', steering=100, speed=30)
