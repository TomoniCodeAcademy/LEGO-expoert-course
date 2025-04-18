#
# AI Camera Sample
# Face Recognition
#


import sys
import time
from hub import port

# import HyskyLens Library
sys.path.append('/projects/mylib000')
from huskylens_lib import Algo
from huskylens_lib import HuskyLens

# setup serial port
port.F.mode(port.MODE_FULL_DUPLEX)
time.sleep(1)   
port.F.baud(9600)

# initialize HusyLens
husky = HuskyLens(port.F)
husky.send_CMD_REQ_ALGO(Algo.FACE_RECOGNITION)

while True:

    # read target info from HuskyLens
    blocks=husky.read_blocks()
    if len(blocks) > 0:
        print('!! find target(face) !!')
        print(blocks)
        type, id, x, y, w, h = blocks[0]
        print(type, id, x, y, w, h)
        if id == 1:
            print('learned face')
        else:
            print('unkown face')
        time.sleep(0.5)
    else:
        print('no target(face)')
        time.sleep(0.5)


