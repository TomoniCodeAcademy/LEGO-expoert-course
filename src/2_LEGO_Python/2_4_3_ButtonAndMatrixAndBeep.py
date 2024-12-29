import time
from spike import PrimeHub
hub = PrimeHub()

counter = 0
while True:
    if hub.left_button.was_pressed():
        hub.speaker.beep(60, 0.5)
        counter -= 1
        hub.light_matrix.write(str(counter))
    if hub.right_button.was_pressed():
        hub.speaker.beep(67, 0.5)
        counter += 1
        hub.light_matrix.write(str(counter))
    
    time.sleep(1)
