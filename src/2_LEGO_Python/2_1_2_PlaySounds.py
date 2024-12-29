#
# file: 2_1_1_play_sounds.py
# 
# 

from spike import App

SOUND_NAME1 = 'Applause 1';
SOUND_NAME2 = 'Applause 2';

app = App()

print(SOUND_NAME1)
app.play_sound(SOUND_NAME1, volume=50)

#print(SOUND_NAME1)
#app.play_sound(SOUND_NAME1, volume=50)


