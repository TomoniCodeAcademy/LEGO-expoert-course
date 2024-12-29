from spike import Motor

motor = Motor('E')
motor.set_default_speed(50)
motor.run_for_degrees(90)

#motor.run_for_degrees(-90)


