#
# yaw angle control (2025/02/28)
#

import sys
import time

from hub import port
from spike import Motor


from spike import MotorPair

SCREEN_WIDTH =320
SCREEN_HEIGHT =240
CENTER_X = int(SCREEN_WIDTH / 2)
CENTER_Y = int(SCREEN_HEIGHT / 2)


sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                # need delay for Port setup ??
port.F.baud(9600)

husky = HuskyLens(port.F)
husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)


motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(30)

def car_spin_right(motor_pair,degrees=10):
    motor_pair.move(degrees,  unit = 'degrees', steering = 100)

def car_spin_left(motor_pair,degrees=10):
    motor_pair.move(-degrees,  unit = 'degrees', steering = 100)


while True:
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h)=blocks[0]
        print('x', x, 'y', y, 'w', w, 'h', h)
        if x > (CENTER_X + 20):
           if x > 240:
               print('turn right 25')            
               car_spin_right(motor_pair,degrees=25)
           else:
               print('turn right 10')            
               car_spin_right(motor_pair,degrees=10)
        elif x < (CENTER_X - 20):
           if x < 80:
               print('turn left  25')            
               car_spin_left(motor_pair,degrees=25)
           else:
               print('turn left 10')            
               car_spin_left(motor_pair,degrees=10)
        else:
           print('xxx')            
           time.sleep(0.5)
    else:
        print('no target(by color)')
        time.sleep(0.1)


