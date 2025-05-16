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


#
# グーチョキパーの勝ち負け判定
#
def judge(humands_hand, legos_hand):
    if humans_hand == legos_hand:
        return 'draw'
    if humans_hand == 'gu':
        if legos_hamd == 'par':
            return 'legos_win'
        else:
            return 'humans_win'
    elif humans_hand == 'choki':
        if legos_hamd == 'gu':
            return 'legos_win'
        else:
            return 'humans_win'
    elif humans_hand == 'par':
        if legos_hamd == 'choki':
            return 'legos_win'
        else:
            return 'humans_win'
    else:  # system error
        return False

def main():
    
    while True:

        # 最初はグー
        janken_ready1()
        hub.light_matrix.show_image(images['gu'])
        time.sleep(0.8)

        # じゃんけんぽん
        janken_ready2()
        rnd = random.randint(0,2)
        lego_hand = hands[rnd]
        print(leg0hand)
        hub.light_matrix.show_image(images[lego_hand])
        time.sleep(1)

        # 人間の手を読み込む
        humans_hand = get_humans_hand()

        # どちらが勝ったか判定する
        winner = judge(humans_hand, lego_hand)

        # 勝敗に従って効果音を鳴らして、点数を計算する
        if winner == 'humans_win':
            pass
        elif ans == 'legos_win':
            pass
        else
            pass

main()
#
#
#
