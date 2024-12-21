#
# conbination Color Recognition and Light Matrix 
# 機能： AIカメラとSPIKE HUBの連携動作
#        AIカメラで色を認識し、LightMatrixを使って、どの座標であるかを表示する
# file:

import time
from spike import PrimeHub
from hub import port

# set library load path
import sys
sys.path.append('/projects/mylib000')

#
# setup UART (using port F)
#
port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                # need delay for Port setup ??
port.F.baud(9600)

#
# setup Huskylens
#
from huskylens_lib import HuskyLens
from huskylens_lib import Algo
husky = HuskyLens(port.F)
# Set the AI camera's recognition algorithm to color recognition mode.
husky.send_CMD_REQ_ALGO(Algo.COLOR_RECOGNITION)  

# initialize Prime HUB
hub = PrimeHub()

led_x = 0
led_y = 0
last_x = 0
last_y = 0
while True:
    #
    # read loop
    #
    object_list = husky.read_blocks()
    print(object_list)  # for debug
    if len(object_list) > 0 and 'block' == object_list[0][0]:
        (_, block_id, x, y, w, h) = object_list[0]
        led_x = int(5 * x / 320)
        led_y = int(5 * y / 240)
        hub.light_matrix.set_pixel(last_x, last_y,brightness=0)  # turn off current lightning LED  
        hub.light_matrix.set_pixel(led_x, led_y)  # turn on LED according to Object position
        last_x = led_x
        last_y = led_y
        print(led_x,led_y)  # for debug
