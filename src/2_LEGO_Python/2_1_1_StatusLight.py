import time
from spike import PrimeHub

COLOR_LIST = ('azure', 'black','blue','cyan','green','orange','pink','red','violet','yellow','white')

hub = PrimeHub()

for color_name in COLOR_LIST:
    print(color_name)
    hub.status_light.on(color_name)
    time.sleep(1)

hub.status_light.on('white')

#
#
#
