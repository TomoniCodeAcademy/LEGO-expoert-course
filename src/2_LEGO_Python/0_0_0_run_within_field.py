#
# Run around only within the field
#

from spike import MotorPair
from spike import ColorSensor

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
        # go straight
        motor_pair.start(speed=60,steering=0)
    else:
        print('outside!!')
        # go back and turn    
        motor_pair.move(amount=90, unit='degrees', steering=0, speed=-40)
        motor_pair.move(amount=90, unit='degrees', steering=100, speed=30)
