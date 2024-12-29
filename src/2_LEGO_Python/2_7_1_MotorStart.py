import time
from spike import Motor

motor = Motor('E')
#motor.set_default_speed(50)

motor.start(50)
time.sleep(5)
motor.start(-50)
time.sleep(5)
motor.stop()





