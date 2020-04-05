from __rOBOT_fUNCTIONS__ import *
#list of the commands thet run this code
list_command=["قصه","داستان","حکایت"]
import random
#as input you should give it how much to play
def story_player(how_much_to_play="complete"):
    list_name=["آهوی لاغر","ابر کوچولو","برف و شادی","بشنو و باور نکن","بوسه ی راسو","جوجه های دارکوب","چکه آب،چکه باران","چه خانه ی زیبایی","خاله جان","خانه جدید خارپشت"]
    MusicPlay(random.choice(list_name)+"()"+str(how_much_to_play))
story_player()