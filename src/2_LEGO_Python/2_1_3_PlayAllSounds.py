#
# file: 1_1_1_play_sounds.py
# 目的： 効果音を全て再生する  (再生するにはLEGO SPIKE IDEと接続されている必要あり)
# 学び： tuple型データから一つずつ値を取り出して繰り返しを行う
#

from spike import App
import time

sound_list = ('Alert','Applause 1','Applause 2','Applause 3','Baa','Bang 1','Bang 2','Basketball Bounce',
'Big Boing','Bird','Bite','Boat Horn 1','Boat Horn 2','Bonk','Boom Cloud','Boop Bing Bop','Bowling Strike',
'Burp 1','Burp 2','Burp 3','Car Accelerate 1','Car Accelerating 2','Car Horn','Car Idle','Car Reverse',
'Car Skid 1','Car Skid 2','Car Vroom','Cat Angry','Cat Happy','Cat Hiss','Cat Meow 1','Cat Meow 2',
'Cat Meow 3','Cat Purring','Cat Whining','Chatter','Chirp','Clang','Clock Ticking','Clown Honk 1',
'Clown Honk 2','Clown Honk 3','Coin','Collect','Connect','Crank','Crazy Laugh','Croak','Crowd Gasp',
'Crunch','Cuckoo','Cymbal Crash','Disconnect','Dog Bark 1','Dog Bark 2','Dog Bark 3','Dog Whining 1',
'Dog Whining 2','Doorbell 1','Doorbell 2','Doorbell 3','Door Closing','Door Creek 1','Door Creek 2',
'Door Handle','Door Knock','Door Slam 1','Door Slam 2','Drum Roll','Dun Dun Dunnn','Emotional Piano',
'Fart 1','Fart 2','Fart 3','Footsteps','Gallop','Glass Breaking','Glug','Goal Cheer','Gong','Growl',
'Grunt','Hammer Hit','Head Shake','High Whoosh','Jump','Jungle Frogs','Laser 1','Laser 2','Laser 3',
'Laughing Baby 1','Laughing Baby 2','Laughing Boy','Laughing Crowd 1','Laughing Crowd 2','Laughing Girl',
'Laughing Male','Lose','Low Boing','Low Squeak','Low Whoosh','Magic Spell','Male Jump 1','Male Jump 2',
'Moo','Ocean Wave','Oops','Orchestra Tuning','Party Blower','Pew','Ping Pong Hit','Plane Flying By',
'Plane Motor Running','Plane Starting','Pluck','Police Siren 1','Police Siren 2','Police Siren 3',
'Punch','Rain','Ricochet','Rimshot','Ring Tone','Rip','Robot 1','Robot 2','Robot 3','Rocket Explosion Rumble',
'Rooster','Scrambling Feet','Screech','Seagulls','Service Announcement','Sewing Machine','Ship Bell',
'Siren Whistle','Skid','Slide Whistle 1','Slide Whistle 2','Sneaker Squeak','Snoring','Snort',
'Space Ambience','Space Flyby','Space Noise','Splash','Sport Whistle 1','Sport Whistle 2',
'Squeaky Toy','Squish Pop','Suction Cup','Tada','Telephone Ring 2','Telephone Ring','Teleport 2',
'Teleport 3','Teleport','Tennis Hit','Thunder Storm','Toliet Flush','Toy Honk','Toy Zing','Traffic',
'Train Breaks','Train Horn 1','Train Horn 2','Train Horn 3','Train On Tracks','Train Signal 1',
'Train Signal 2','Train Start','Train Whistle','Triumph','Tropical Birds','Wand','Water Drop',
'Whistle Thump','Whiz 1','Whiz 2','Window Breaks','Win','Wobble','Wood Tap','Zip')

# アプリ(App)の初期化
app = App()

for sound_name in sound_list:
    print(sound_name)
    if True:  # if you are patient.
        app.play_sound(sound_name, volume=50)
    else:  # if you are impatient and can't tolerate waiting.
        app.start_sound(sound_name, volume=50)
        time.sleep(1)  
