from __rOBOT_fUNCTIONS__ import *
def find_singer():
    #you should put the list of singers and their songs here
    #it should be a 2-D list and like the below sentence
    #[[song name.mp3,singer]]
    list_songs_and_singers=[[["AronAfshar_1.mp3"],"آرون افشار"],[["HamedBahram_1.mp3"],"حامد بهرام"],[["BehnamBani_1.mp3"],"بهنام یانی"]]
    while True:   
        list_artist=random.choice(list_songs_and_singers)
        MusicPlay(random.choice(list_artists[0])+"()30")
        Input=CompleteVoiceAnalyse()
        if Input!=list_artists[1]:
            TTS("اشتباه بود","fa")
        elif Input=="بیرون":
            break
        else:
            TTS("درست بود","fa")
