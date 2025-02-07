#
# test code for LEGO SPIKE and HuskyLens 
#
# function:  
# Rotate the AI-Car to search for the tag 
# Move forward to the detected tag
# Stop the AI-CAR  when reached to the tag

import sys
from hub import port
import time

SCREEN_WIDTH =320
CENTER_X = int(SCREEN_WIDTH / 2)

sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

from spike import MotorPair
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(20)

port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                # need delay for Port setup ??
port.F.baud(9600)

husky = HuskyLens(port.F)
husky.send_CMD_REQ_ALGO(Algo.TAG_RECOGNITION)

def turn_and_find():
    # turn right
    for _ in range(20):
        motor_pair.move(90, unit='degrees', steering=100)
        time.sleep(0.5) # wait for stability
        info = husky.read_tags()
        print(info)
        if len(info)>0:
            if info[0][0]=='block' and info[0][1]==1:
                print('find target')
                return True
    print('can not find target')
    return False

def align_target():
    info = husky.read_tags()
    if len(info)>0:
        if info[0][0]=='block' and info[0][1]==1:
            (_,_,x,y,w,h) = info[0]
            if abs(CENTER_X -x ) < 20:
                return True
            if x > CENTER_X:
                motor_pair.move(10, unit='degrees', steering=80)
                return True
            if x < CENTER_X:
                motor_pair.move(10, unit='degrees', steering=-80)
                return True
    return False

while True:
    info = husky.read_tags()
    print(info)
    if len(info)>0:
        if info[0][0]=='block' and info[0][1]==1:
            (_,_,x,y,w,h) = info[0]
            if w > 50 or h > 50:
                print('complete!')
                break             # approaching the target is complete
    state = align_target()
    if state is False:
        turn_and_find()
    else:
        motor_pair.move(180,unit='degrees',steering=0)


from spike import PrimeHub
hub = PrimeHub()
hub.speaker.beep(80, 0.3)
hub.speaker.beep(85, 0.3)
