#
#
#  Sample Program
#     Camera tilt controll
#     2025/02/28
#
#  Gear settings:
#  camera -> Black -> gray -> brown -> servo
#
import sys
import time

from hub import port
from spike import Motor

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


motor = Motor('E')
motor.set_default_speed(30)

def move_camera_up(servo,degrees=10):
    servo.run_for_degrees(degrees)

def move_camera_down(servo,degrees=10):
    servo.run_for_degrees(-degrees)

while True:
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h)=blocks[0]
        print('x', x, 'y', y, 'w', w, 'h', h)
        if y > (CENTER_Y + 10): 
            if y > 210:
                print('down 30')
                move_camera_down(motor,degrees=30)
            elif y > 180:
                print('down 20')
                move_camera_down(motor,degrees=20)
            else:
                print('down 10')
                move_camera_down(motor,degrees=10)
        elif y < (CENTER_Y - 10): 
            if y < 30:
                print('up 30')
                move_camera_up(motor,degrees=30)
            elif y < 60:
                print('up 20')
                move_camera_up(motor,degrees=20)
            else:
                print('up 10')
                move_camera_up(motor,degrees=10)
        else:
             print('zzz')
             time.sleep(0.5)
    else:
        print('no target(by color)')
        time.sleep(0.1)


