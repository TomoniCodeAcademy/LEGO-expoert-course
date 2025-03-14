#
# find ball and approach it 
# final version (v1.0)
# date: 2025/3/14
# (1) Searching for the ball while circling
# (2) Approach the ball while adjusting to face it directly
# (3) repeat (1),(2)


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

def car_spin_degrees(amount=30, speed=20, steering=100):
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


def search_ball():
    is_found = False

    print('searching... camera down(for ball)')
    set_camera_down(motor)
    car_spin(speed=10, times=0)
    for _ in range(70):
        if is_target_found():
            is_found = True
            print('found target')
            beep_bp()
            car_stop()
            return is_found

    print('searching... camera lower(for ball)')
    set_camera_horizontal(motor, position=150)
    car_spin(speed=10, times=0)
    for _ in range(70):
        if is_target_found():
            is_found = True
            print('found target')
            car_stop()
            beep_bp()
            return is_found

    print('searching... camera horizontal(for ball)')
    set_camera_horizontal(motor, position=180)
    car_spin(speed=10, times=0)
    for _ in range(70):
        if is_target_found():
            is_found = True
            print('found target')
            car_stop()
            beep_bp()
            return is_found

    car_stop()
    return is_found




def approach_ball():
    while True:            # for _ in range(10):
        blocks = husky.read_blocks()
        if len(blocks) == 0:
            print('lost')
            beep_down()
            motor_pair.stop()
            return False

        # ball is in screen
        (obj, id, x, y, w, h) = blocks[0]
        print("ball position:", x, y, w, h)
        adjust_camera(y)
        if w < 50:
            speed = 20
        elif w > 130:
            print('reached BALL!!!')
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





#
#adjust camera angle
#y:target position in Screen
#
def adjust_camera(y):
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



#
# camera control functions
#
def set_camera_horizontal(servo, position=180):
    servo.run_to_position(position)

def set_camera_down(servo, position=120):
    servo.run_to_position(position)

def set_camera_up(servo, position=270):
    servo.run_to_position(position)

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




def beep_down():
    prime_hub.speaker.beep(80, 0.2)
    prime_hub.speaker.beep(77, 0.2)


def beep_bp():
    prime_hub.speaker.beep(77, 0.2)                
    prime_hub.speaker.beep(80, 0.2)

def beep_px():
    prime_hub.speaker.beep(82, 0.2)
    prime_hub.speaker.beep(85, 0.2)



while True:
    print('search ball')
    is_found = search_ball()
    if is_found:
        print('ball is found')
        # check over run
        if is_target_found():
            print('not over run')
        else:
            print('over run, so spin back')
            car_spin_degrees(amount=15,  steering=-100)
            if is_target_found():
                print('adjust succeed')
            else:
                print('adjust failed')

        approach_ball()

    else:
        print('ball is not found')

