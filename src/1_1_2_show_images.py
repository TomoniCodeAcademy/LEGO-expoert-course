#
# file: 1_1_2_show_images.py
# 目的： LEDパターンを全て表示する
# 学び： iter型データを使って繰り返しを行う
#

from spike import PrimeHub
import time

image_list = ('ANGRY', 'ARROW_E', 'ARROW_N', 'ARROW_NE', 'ARROW_NW', 
        'ARROW_S', 'ARROW_SE', 'ARROW_SW', 'ARROW_W', 'ASLEEP',
        'BUTTERFLY', 'CHESSBOARD', 'CLOCK1', 'CLOCK10', 'CLOCK11',
        'CLOCK12', 'CLOCK2', 'CLOCK3', 'CLOCK4', 'CLOCK5', 'CLOCK6',
        'CLOCK7', 'CLOCK8', 'CLOCK9', 'CONFUSED', 'COW', 'DIAMOND', 
        'DIAMOND_SMALL', 'DUCK', 'FABULOUS', 'GHOST', 'GIRAFFE', 
        'GO_RIGHT', 'GO_LEFT', 'GO_UP', 'GO_DOWN', 'HAPPY', 'HEART', 
        'HEART_SMALL', 'HOUSE', 'MEH', 'MUSIC_CROTCHET', 'MUSIC_QUAVER', 
        'MUSIC_QUAVERS', 'NO', 'PACMAN', 'PITCHFORK', 'RABBIT', 
        'ROLLERSKATE', 'SAD', 'SILLY', 'SKULL', 'SMILE', 'SNAKE', 
        'SQUARE', 'SQUARE_SMALL', 'STICKFIGURE', 'SURPRISED', 'SWORD', 
        'TARGET', 'TORTOISE', 'TRIANGLE', 'TRIANGLE_LEFT', 'TSHIRT',
        'UMBRELLA', 'XMAS', 'YES')



# HUBの初期化
hub = PrimeHub()

for image_name in image_list:
    print(image_name)
    hub.light_matrix.show_image(image_name)
    time.sleep(1)  

# finally set HAPPY
hub.light_matrix.show_image('HAPPY')

#
#
#