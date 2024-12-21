from spike import App
from spike import PrimeHub

import time
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
husky = HuskyLens(port.F)

from huskylens_lib import Algo
husky.send_CMD_REQ_ALGO(Algo.FACE_RECOGNITION)

# init App
app = App()

while True:
    #
    # read loop
    #
    object_list = husky.read_blocks()
    print(object_list)
    if len(object_list) > 0 and 'block' == object_list[0][0]:
        (_,block_id, x, y, w, h) = object_list[0]
        if block_id == 1:
            print('i know about you!!')
            app.play_sound('Connect', volume=50)
        else:
            print('Who are you?')
            app.play_sound('Big Boing', volume=50)
