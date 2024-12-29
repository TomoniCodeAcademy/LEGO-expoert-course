from spike import MotorPair

motor_pair = MotorPair('A', 'B')
motor_pair.move(10, unit='cm', speed=30)

# to stop
#motor_pair.stop()