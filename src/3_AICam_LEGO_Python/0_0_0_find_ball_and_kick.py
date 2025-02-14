#
# demo find ball and approach
#    2025/2/14 v0.01
#
#
# function
#(1) find target
#(1) approach
#(3) no kick


import sys
from hub import port
import time

from spike import MotorPair, Motor

sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

SCREEN_WIDTH =320
CENTER_X = int(SCREEN_WIDTH / 2)

husky = None
motor_pair = None
motor_c = None

from spike import DistanceSensor
distance_sensor = DistanceSensor('D')

from spike import PrimeHub
hub = PrimeHub()


def setup():

    global husky
    global motor_pair
    global motor_c

    motor_pair = MotorPair('A', 'B')
#    motor_c = Motor('C')

    port.F.mode(port.MODE_FULL_DUPLEX)
    time.sleep(1)                # need delay for Port setup ??
    port.F.baud(9600)
    husky = HuskyLens(port.F)
    husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)

def find_target():
    blocks=husky.read_blocks()

    if len(blocks) > 0:
        (obj,id,x,y,w,h) = blocks[0]
        if id == 1:
            return True
    return False

def get_target_info():
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        (obj,id,x,y,w,h) = blocks[0]
        return (obj,id,x,y,w,h)
    return None

def car_move_forward(speed=20,times=2,steering=0):
    motor_pair.start(speed = speed,steering=steering)
    if times != 0:
        time.sleep(times)
        motor_pair.stop()

def car_move_back(speed=20, times=2,steering=0):
    car_move_forward(speed*-1,times,steering)

def car_approach_target():
    car_move_forward(speed=20,times=1.5)

def car_spin(speed=20, times=3):
    motor_pair.start(speed=speed,steering=100)
    if times != 0:
        time.sleep(times)
        motor_pair.stop()

def car_stop():
    motor_pair.stop()

def search_target():
    found = False
    car_spin(speed=20, times=0)
    for _ in range(40):
        if find_target():
            found = True
            break
        else:
            continue
    car_stop()
    return found

def car_random_walk():
    print('random walk')
    car_spin(speed=20, times=1)
    car_move_forward(speed=20,times=3)
    #car_move_back(speed=20,times=0.5)

def kick():
    print('kick')
    return
    #motor_c.run_for_degrees(200,speed=100)  # no kick


def beep():
    hub.speaker.beep(77, 0.2)
    hub.speaker.beep(80, 0.2)


retry_count = 0
def main_loop_no_use():
    global retry_count
    while True:
        if find_target():
            retry_count=0
            car_approach_target()
            kick()
        else:
            search_target()
            car_random_walk()



setup()


found = False
prev_found = False

#main()
print('!!start!!')
while True:
    prev_found = found
    found = search_target()
    if found:
        print('find!!')
        if prev_found is not True:
            beep()
        info = get_target_info()
        if info is None:
            car_move_forward(speed=20,times=2,steering=0)
        else:
            (obj,id,x,y,w,h) = info
            if x < 100:
                car_move_forward(speed=20,times=2,steering=-20)
            elif x > 200:  
                car_move_forward(speed=20,times=2,steering=20)
            else:
                car_move_forward(speed=20,times=2,steering=0)

    else:
        print('fot find')
        dist = distance_sensor.get_distance_cm()
        print(dist)
        if dist is None or dist > 5:
            car_move_forward(speed=20,times=2)
        else:
            car_move_back(speed=20,times=2)

