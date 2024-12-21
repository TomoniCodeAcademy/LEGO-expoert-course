from spike import PrimeHub
import time

CLOCK_IMAGES = ('CLOCK1', 'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6', 
                'CLOCK7', 'CLOCK8', 'CLOCK9', 'CLOCK10', 'CLOCK11', 'CLOCK12')
                
hub = PrimeHub()
for clock_image in CLOCK_IMAGES:
    hub.light_matrix.show_image(clock_image)
    time.sleep(0.1)
        
