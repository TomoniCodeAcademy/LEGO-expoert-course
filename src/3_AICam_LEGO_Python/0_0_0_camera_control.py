#
# simple camera control
# gear settings
# Camera -> black -> gray -> brown -> Servo
#
from spike import Motor

motor = Motor('E')
motor.set_default_speed(20)

def set_camera_horizontal(servo):
    servo.run_to_position(90)

def set_camera_up(servo):
    servo.run_to_position(180)

def set_camera_down(servo):
    servo.run_to_position(15)

def move_camera_up(servo,degrees=10):
    servo.run_for_degrees(degrees)

def move_camera_down(servo,degrees=10):
    servo.run_for_degrees(-degrees)


motor.run_to_position(90)
motor.run_to_position(15)
motor.run_to_position(120)

motor.run_for_degrees(10)
motor.run_for_degrees(-10)


