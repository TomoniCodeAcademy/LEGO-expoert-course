#
# demo  find and kick ball
#       2025/2/14 v0.01
#
#
# function
#   (1) find target
#   (1) approach
#   (3) kick


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
    
def setup():

    global husky
    global motor_pair
    global motor_c

    motor_pair = MotorPair('A', 'B')
    motor_c = Motor('C')
    
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

def car_move_forward(speed=20,times=2):
   motor_pair.start(speed = speed)
   if times != 0:
      time.sleep(times)
      motor_pair.stop()

def car_move_back(speed=20, times=2):
   car_move_forward(speed*-1,times)

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
   car_spin(speed=20, times=0)
   for _ in range(50):
      if find_target():
          break
      else:
          continue
   car_stop()

def car_random_walk():
   print('random walk')
   car_move_forward(speed=20,times=0.5)
   car_spin(speed=20, times=0.5)
   car_move_back(speed=20,times=0.5)

def kick():
   print('kick')
   return
   motor_c.run_for_degrees(400,'degrees',speed=100)

retry_count = 0
def main_loop():
    global retry_count
    while True:
       if find_target():
           retry_count=0
           car_approach_target()
           kick()
       else:
           retry_count += 1
           search_target()
       if retry_count > 2:
           car_random_walk()


def main():
   setup()
   main_loop()

