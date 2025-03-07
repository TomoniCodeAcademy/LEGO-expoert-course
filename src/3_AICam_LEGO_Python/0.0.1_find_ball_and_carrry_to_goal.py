#
# find ball and carry to goal
# date: 2025/xxxxxx
# (1) Search for the target ball while rotating.
# (2) Approach the target while steering to keep it centered on the screen.
# (3) Stop when within a certain proximity to the target.
# date: 2025/03/07 13:00
# (4) find TAG and approach
# (5) Repeat two processes

import sys
from hub import port
from spike import Motor
from spike import MotorPair
import time
import random

from spike import PrimeHub
prime_hub = PrimeHub()


#
# setup servo motors
#

# set motor for Camera angle
motor = Motor('E')
motor.set_default_speed(30)

# set motor_pair for car move
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(30)

SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
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
time.sleep(0.5)

def car_stop():
    motor_pair.stop()

def car_spin(speed=20, times=3,steering=100):
    motor_pair.start(speed=speed,steering=steering)
    if times != 0:
        time.sleep(times)
        motor_pair.stop()

def car_spin_degrees(amount=30, speed=20,steering=100):
    motor_pair.move(amount,unit='degrees',speed=speed,steering=steering)

def is_target_found(with_target_info=False):
    blocks=husky.read_blocks()
    # print(blocks)
    if len(blocks) > 0:
        (obj,id,x,y,w,h) = blocks[0]
        if id == 1:
            print('is_target_found', obj,id,x,y,w,h)
            if with_target_info:
                return(True, obj,id,x,y,w,h)
            else:
                return True
    if with_target_info:
        return (False,())
    else:
        return False



def search_TAG():
    is_found = False

    # set Algo to TAG_RECOGNITION
    husky.send_CMD_REQ_ALGO(Algo.TAG_RECOGNITION)
    time.sleep(0.5)

    print('set camera horizontal')
    set_camera_horizontal(motor)
    car_spin(speed=8, times=0)
    for _ in range(70):
        target_check =  is_target_found()
        if target_check == True:
            is_found = True
            print('found target')
            car_stop()
            beep_bp()
            # if target is not in screen then spin backword
            blocks=husky.read_blocks()
            print(blocks)
            if len(blocks) > 0:
                print('TAG is inside screen')
            else:
                print('over run so spin backword')
                car_spin_degrees(speed = 10, steering = -100)
            return True
    car_stop()
    return is_found



def search_target():
    is_found = False

    print('searching... camera down')
    set_camera_down(motor)
    car_spin(speed=10, times=0)
    for _ in range(70):
        if is_target_found():
            is_found = True
            print('found target')
            beep_bp()
            car_stop()
            return True

    print('searching... camera horizontal')
    set_camera_horizontal(motor)
    car_spin(speed=10, times=0)
    for _ in range(70):
        if is_target_found():
            is_found = True
            print('found target')
            car_stop()
            beep_bp()
            return True

    print('searching... random move...')
    nth_action = int(random.random() * 2)
    if  nth_action == 1:
        print('searching... go')
        motor_pair.move(180,unit = 'degrees', steering = 0, speed=10)
    else:
        print('searching...back')
        motor_pair.move(-180,unit = 'degrees', steering = 0, speed=10)

    return is_found

#
# car control functions
#
def car_spin_right(motor_pair,degrees=10):
    motor_pair.move(degrees,unit = 'degrees', steering = 100)

def car_spin_left(motor_pair,degrees=10):
    motor_pair.move(-degrees,unit = 'degrees', steering = 100)

#
# camera control functions
#
def move_camera_up(servo,degrees=10):
    if servo.get_position() > 270:
        print('can not up, so skip')
    else:
        servo.run_for_degrees(degrees)

def move_camera_down(servo,degrees=10):
    if servo.get_position() < 90:
        print('can not down, so skip')
    else:
        servo.run_for_degrees(-degrees)

def set_camera_horizontal(servo):
    servo.run_to_position(180)

def set_camera_down(servo):
    servo.run_to_position(90)

def set_camera_up(servo):
    servo.run_to_position(270)
    
#
#  y:  target position in Screen
#    
def camera_angle(y):
    if y > (CENTER_Y + 10):
        if y > 210:
            move_camera_down(motor,degrees=50)
        elif y > 180:
            move_camera_down(motor,degrees=30)
        else:
            move_camera_down(motor,degrees=10)
    elif y < (CENTER_Y - 10):
        if y < 30:
            move_camera_up(motor,degrees=50)
        elif y < 60:
            move_camera_up(motor,degrees=30)
        else:
            move_camera_up(motor,degrees=10)

def beep_bp():
    prime_hub.speaker.beep(77, 0.2)                
    prime_hub.speaker.beep(80, 0.2)

def beep_px():
    prime_hub.speaker.beep(82, 0.2)
    prime_hub.speaker.beep(85, 0.2)

def find_and_approach_ball():
  while True:# for _ in range(10):
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h)=blocks[0]
        print('x', x, 'y', y, 'w', w, 'h', h)
        camera_angle(y)
        if w < 50:
            speed = 30
        elif w > 130:
            print('reached!!!')
            beep_px()
            motor_pair.stop()
            speed = 0
            break
        elif w > 100:
            print('speed down(4)')
            speed = 4
        elif w > 80:
            print('speed down(5)')
            speed = 5
        elif w > 70:
            print('speed down(6)')
            speed = 6
        else:
            speed = 20
        if x > (CENTER_X + 20):
            motor_pair.start(speed=speed, steering=20)
        elif x < (CENTER_X - 20):
            motor_pair.start(speed=speed, steering=-20)
        else:
            motor_pair.start(speed=speed, steering=0)
    else:
        print('lost')
        search_target()



#husky.send_CMD_REQ_ALGO(Algo.TAG_RECOGNITION)
#utime.sleep(0.5)
# dummy read
#print('dummy read')
#for _ in range(3):
#   blocks=husky.read_blocks()
#   print(blocks)
#   utime.sleep(0.5) 

print('-------------------------')
print(is_target_found())
print('-------------------------')




def approach_TAG():
  while True:
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h)=blocks[0]
        print('x', x, 'y', y, 'w', w, 'h', h)
        if w < 50:
            speed = 30
        elif w > 140:
            print('reached!!!')
            beep_px()
            motor_pair.stop()
            speed = 0
            break
        elif w > 100:
            print('speed down(4)')
            speed = 6
#        elif w > 80:
#            print('speed down(5)')
#            speed = 5
#        elif w > 70:
#            print('speed down(6)')
#            speed = 6
        else:
            speed = 20
        if x > (CENTER_X + 20):
            motor_pair.start(speed=speed, steering=20)
        elif x < (CENTER_X - 20):
            motor_pair.start(speed=speed, steering=-20)
        else:
            motor_pair.start(speed=speed, steering=0)



while True:

    husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)
    time.sleep(0.5)

    find_and_approach_ball()
    motor_pair.stop()

    find_flag = search_TAG()
    if find_flag:
        approach_TAG()
#car_spin_degrees(speed = 10, steering = -100)
