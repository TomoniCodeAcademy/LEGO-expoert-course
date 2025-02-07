# follow  pinpon ball (yellow)
#  2025/2/7
#

import time
import sys

from spike import PrimeHub
hub = PrimeHub()

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


def adjust_angle_camera(husky, motor):
    # start rotate
    blocks = husky.read_blocks()
    if(len(blocks) > 0):
        (obj,id,x,y,w,h) = blocks[0]
        #print(y)
        if(y > 180):
            #print('up2')
            motor.run_for_degrees(-20,speed=20)
        elif(y > 120):
            #print('up')
            motor.run_for_degrees(-10,speed=20)
        elif(y < 50):
            #print('down2')
            motor.run_for_degrees(20,speed=20)
        elif(y < 100):
            #print('down')
            motor.run_for_degrees(10,speed=20)


def adjust_angle_car(husky, motor):
    # start rotate
    blocks = husky.read_blocks()
    if(len(blocks) > 0):
        (obj,id,x,y,w,h) = blocks[0]
        print(x)
        if(x > 180):
            motor_pair.move(13,unit='degrees',speed=10,steering=100)
        elif(x < 140):
            motor_pair.move(-13,unit='degrees',speed=10,steering=100)



#----------------------------
#
#AI Camera angle control
#
#    set_camera_angle(<motor>,<angle>)
#    angle := ( 'horizontal' | 'up' | 'down' )
#
#----------------------------
def set_camera_angle(motor, direction='horizontal'):

    position = motor.get_position()

    if direction == 'horizontal':
        motor.run_to_position(0, speed=20)

    elif direction == 'up':# target position is 90
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

    elif direction == 'lightdown':
        if position >= 200 and position <= 300 :
            pass
        else:
            if position > 0:
                motor.run_to_position(0, speed=20)
            motor.run_for_degrees(-50, speed=20)



def search_ball(husky, motor_pair, motor_e):

    # set camera angle down
    set_camera_angle(motor_e, 'lightdown')

    # start rotate
    motor_pair.start(steering=100, speed=15)
    while True:
        blocks = husky.read_blocks()
        if(len(blocks) > 0):
            print('find ball')
            motor_pair.stop()
            #hub.speaker.beep(85, 0.1)
            #hub.speaker.beep(90, 0.1)
            break


def follow_ball(husky, motor_pair, motor_e):

    blocks = husky.read_blocks()
    if len(blocks) == 0:
        set_camera_angle(motor_e, direction='horizontal')
        search_ball(husky, motor_pair, motor_e)
    else:
        (obj,id,x,y,w,h) = blocks[0]
        print('w:',w)
        if w > 100:
            return
        
        adjust_angle_camera(husky, motor_e)
        adjust_angle_car(husky, motor_pair)
        if w < 20:
            motor_pair.move(360,unit='degrees',speed=30,steering=0)
        elif w < 80:
            motor_pair.move(180,unit='degrees',speed=20,steering=0)
        elif w < 90:
            motor_pair.move(90,unit='degrees',speed=20,steering=0)
        else: 
            motor_pair.move(30,unit='degrees',speed=20,steering=0)

set_camera_angle(motor_e, direction='horizontal')
while True:
    follow_ball(husky, motor_pair, motor_e)


#
#
