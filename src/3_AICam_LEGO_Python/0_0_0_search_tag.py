#
# search TAG
#

import time
import sys

from hub import port
from spike import MotorPair
from spike import Motor   


#
# HuskyLens libraries
#
sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                        # need delay for Port setup ??
port.F.baud(9600)
husky = HuskyLens(port.F)
husky.send_CMD_REQ_ALGO(Algo.TAG_RECOGNITION)

#
# set up motor 
#
motor_pair = MotorPair('A', 'B')
motor_e = Motor('E')


#
#
#
#


from spike import PrimeHub
hub = PrimeHub()

def search_tag(husky, motor_pair, motor_e):

   # set camera angle down
   set_camera_angle(motor_e, 'lightup')

   # start rotate
   motor_pair.start(steering=100, speed=10)
   while True:
       blocks = husky.read_blocks()
       if(len(blocks) > 0):
            print('find ball')
            motor_pair.stop()
            hub.speaker.beep(85, 0.1)
            hub.speaker.beep(90, 0.1)
            break


#----------------------------
#
#  AI Camera angle control
#
#     set_camera_angle(<motor>,<angle>)
#     angle := ( 'horizontal' | 'up' | 'down' )
#
#----------------------------
def set_camera_angle(motor, direction='horizontal'):

    position = motor.get_position()

    if direction == 'horizontal':
          motor.run_to_position(0, speed=20)

    elif direction == 'lightup':  # target position is 90
         if position >= 80 and position <= 90:
               pass
         else:
             if position >= 200:
                  motor.run_to_position(0, speed=20)
             motor.run_to_position(45, speed=20)

    elif direction == 'up':  # target position is 90
         if position >= 80 and position <= 90:
               pass
         else:
             if position >= 200:
                  motor.run_to_position(0, speed=20)
             motor.run_to_position(90, speed=20)

    elif direction == 'down':
         if position >= 200 and position <= 300 :
              pass
         else:
             if position > 0:
                  motor.run_to_position(0, speed=20)
             motor.run_for_degrees(-100, speed=20)

    else:
        print("??",direction)



search_tag(husky, motor_pair, motor_e)



#
#
#
