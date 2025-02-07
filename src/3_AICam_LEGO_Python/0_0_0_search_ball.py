#
#
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
husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)

#
# set up motor 
#
motor_pair = MotorPair('A', 'B')
motor_e = Motor('E')


#
#
#
def search_ball(husky, motor_pair, motor_e)

   # set angle
   set_camera_angle(motor_e) # set horizontal
   set_camera_angle(motor_e, 'down')

   # start rotate
   motor_pair.start(steering=100, speed=20)
   while True:
       blocks = husky.read_blocks()
       if(len(blocks) > 0)
            motor_pair.stop()

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

    elif direction == 'up':  # target position is 90
         if position >= 80 and position <= 90:
               pass
         else:
             if position >= 200:
                  motor.run_to_position(0, speed=20)
             motor.run_to_position(90, speed=20)

    elif direction == 'down':
         if position >= 200:
              pass
         else:
             if position > 0:
                  motor.run_to_position(0, speed=20)
             motor.run_for_degrees(-100, speed=20)

search_ball(husky, motor_pair, motor_e)
