#
#  play sound with gu/choki/par
#

import time
import sys
from hub import port
from spike import PrimeHub


#
# HuskyLens libraries
#
sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)                        
port.F.baud(9600)
husky = HuskyLens(port.F)
husky.send_CMD_REQ_ALGO(Algo.OBJECT_CLASSIFICATION)


# initialize hub for play sound
hub = PrimeHub()

while True:
    blocks = husky.read_blocks()
    #print(blocks)
    if len(blocks) > 0:
        target = blocks[0][1] 
        if target > 1:
            print('target...', target)
            if target == 2:      # gu
                hub.speaker.beep(65, 0.1)
            if target == 3:      # choki
                hub.speaker.beep(70, 0.1)
            if target == 4:      # par
                hub.speaker.beep(75, 0.1)
                

