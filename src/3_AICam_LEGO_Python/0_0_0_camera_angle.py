#----------------------------
#
#  AI Camera angle control
#
#     set_camera_angle(<motor>,<angle>)
#     angle := ( 'horizontal' | 'up' | 'down' )
#
#----------------------------
def set_camera_angle(motor, direction='horizontal'):

    position = motor.get_position()

    if direction == 'horizontal':
          motor.run_to_position(0, speed=20)

    elif direction == 'up':  # target position is 90
         if position >= 80 and position <= 90:
               pass
         else:
             if position >= 200:
                  motor.run_to_position(0, speed=20)
             motor.run_to_position(90, speed=20)

    elif direction == 'down':
         if position >= 200:
              pass
         else:
             if position > 0:
                  motor.run_to_position(0, speed=20)
             motor.run_for_degrees(-100, speed=20)


#
# test
#
from spike import Motor

def test():
   motor_e = Motor('E')
   set_camera_angle(motor_e)
   set_camera_angle(motor_e, 'up')
   set_camera_angle(motor_e, 'down')
   set_camera_angle(motor_e, 'up')
   set_camera_angle(motor_e, 'up')
   set_camera_angle(motor_e, 'horizontal')
   set_camera_angle(motor_e, 'down')
   set_camera_angle(motor_e, 'down')
   set_camera_angle(motor_e)



