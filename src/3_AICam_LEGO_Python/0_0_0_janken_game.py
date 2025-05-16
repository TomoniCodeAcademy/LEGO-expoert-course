#
# file: 1_1_2_show_images.py
# 目的： LEGO+AI MAMとじゃんけんゲームをする
# 学び： オブジェクト認識で、じゃんけんの手を認識する
#        LEGOが出している手とどっちが勝っているか判定する
#        勝敗を数える、表示する
#

from spike import PrimeHub
import time

hands = ('gu', 'choki', 'par')
images = {'gu': 'SQUARE_SMALL', 'choki':'YES', 'par':'NO'}


# HUBの初期化
hub = PrimeHub()

import random

# タイミングを合わせるためリズムを流す
def janken_ready1():
    hub.speaker.beep(note=65, seconds=0.2)
    time.sleep(0.3)
    hub.speaker.beep(note=65, seconds=0.2)
    time.sleep(0.3)
    hub.speaker.beep(note=75, seconds=0.2)


def janken_ready2():
    hub.speaker.beep(note=65, seconds=0.2)
    time.sleep(0.1)
    hub.speaker.beep(note=65, seconds=0.4)
    time.sleep(0.2)
    hub.speaker.beep(note=65, seconds=0.1)
    time.sleep(0.1)
    hub.speaker.beep(note=75, seconds=0.2)



while True:

    # 最初はグー
    janken_ready1()
    hub.light_matrix.show_image(images['gu'])
    time.sleep(0.8)

    # じゃんけんぽん
    janken_ready2()
    rnd = random.randint(0,2)
    hand = hands[rnd]
    print(hand)
    hub.light_matrix.show_image(images[hand])
    time.sleep(1)
#
#
#
