#
# play sound with servo
#

from spike import Motor
from spike import PrimeHub
hub = PrimeHub()

motor = Motor('D')
motor.set_degrees_counted(0)
while True:
    pos = motor.get_position()
    tone = 44 + int((123-44)*pos/360)
    print('tone',tone)
    hub.speaker.beep(tone, 0.1)
