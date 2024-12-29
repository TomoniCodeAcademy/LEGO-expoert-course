from spike import MotorPair

motor_pair = MotorPair('A', 'B')
motor_pair.set_default_speed(30)

# Rotate the servo shaft 90 degrees to the right.
# (not turning the car 90 degrees!!)

motor_pair.move(90, unit='degree', steering=100)

# motor_pair.move(90, unit='degree', steering = -100)