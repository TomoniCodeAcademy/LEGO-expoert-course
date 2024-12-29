import time
from spike import PrimeHub
hub = PrimeHub()

counter = 0
while True:
    if hub.left_button.was_pressed():
        counter -= 1
    if hub.right_button.was_pressed():
        counter += 1
    print(counter)
    time.sleep(1)
