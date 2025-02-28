#
# target alignment control (2025/02/28)
# description:
#   (1) find target (ball)
#   (2) move car and camera to align target
#   (3) if target is lost, then search target with spin a car
#   (4) Use a beep to indicate activity
#
import sys
import time

from hub import port
from spike import Motor
from spike import MotorPair

from spike import PrimeHub
prime_hub = PrimeHub()


SCREEN_WIDTH = 320
SCREEN_HEIGHT = 240
CENTER_X = int(SCREEN_WIDTH / 2)
CENTER_Y = int(SCREEN_HEIGHT / 2)

#
# setup HuskyLens
#
sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                # need delay for Port setup ??
port.F.baud(9600)

husky = HuskyLens(port.F)
husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)


#
# setup servo motors
#

# set motor for Camera angle
motor = Motor('E')
motor.set_default_speed(30)

# set motor_pair for car move
motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(30)


#
# car control functions
#
def car_spin_right(motor_pair,degrees=10):
    motor_pair.move(degrees,  unit = 'degrees', steering = 100)

def car_spin_left(motor_pair,degrees=10):
    motor_pair.move(-degrees,  unit = 'degrees', steering = 100)

#
# camera control functions
#
def move_camera_up(servo,degrees=10):
    servo.run_for_degrees(degrees)

def move_camera_down(servo,degrees=10):
    servo.run_for_degrees(-degrees)

def set_camera_horizontal(servo):
    servo.run_to_position(90)

def set_camera_down(servo):
    servo.run_to_position(20)

def set_camera_up(servo):
    servo.run_to_position(160)


#
# car yaw angle adjust
#
def car_yaw_adjust(motor_pair, x):
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

#
# camera angle adjust
#
def camera_angle_adjust(motor, y):
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


def car_stop():
    motor_pair.stop()

def car_spin(speed=20, times=3):
    motor_pair.start(speed=speed,steering=100)
    if times != 0:
        time.sleep(times)
        motor_pair.stop()

def is_target_found():
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h) = blocks[0]
        if id == 1:
            return True
    return False

def search_target():
    is_found = False
    set_camera_down(motor)
    car_spin(speed=20, times=0)
    for _ in range(40):
        if is_target_found():
            is_found = True
            break
    car_stop()
    return is_found

def beep_bp():
    prime_hub.speaker.beep(90,0.1)
    prime_hub.speaker.beep(95,0.2)

def beep_pb():
    prime_hub.speaker.beep(85,0.1)
    prime_hub.speaker.beep(80,0.1)

while True:
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h)=blocks[0]
        print('x', x, 'y', y, 'w', w, 'h', h)
        car_yaw_adjust(motor_pair, x)
        camera_angle_adjust(motor, y)
    else:
        print('no target(by color)')
        beep_pb()
        is_found = search_target()
        if is_found:
            beep_bp()
