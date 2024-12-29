import time
from spike import PrimeHub
hub = PrimeHub()

counter = 0
while True:
    if hub.left_button.was_pressed():
        counter -= 1
        hub.light_matrix.write(str(counter))
    if hub.right_button.was_pressed():
        counter += 1
        hub.light_matrix.write(str(counter))
    
    time.sleep(1)
