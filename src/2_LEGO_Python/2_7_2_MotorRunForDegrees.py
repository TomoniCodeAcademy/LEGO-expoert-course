from spike import Motor

motor = Motor('E')
motor.set_default_speed(50)
motor.run_for_degrees(90)
motor.get_position()

#motor.run_for_degrees(-90)

motor.run_to_position(90)
motor.run_to_position(0)

