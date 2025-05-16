#
#  object classification
#

import time
from hub import port

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
husky.send_CMD_REQ_ALGO(Algo.OBJECT_CLASSIFICATION)

while True:
    print(husky.read_blocks())
