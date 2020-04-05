from __rOBOT_fUNCTIONS__ import *
def find_singer():
    #you should put the list of singers and their songs here
    #it should be a 2-D list and like the below sentence
    #[[song name.mp3,singer]]
    list_songs_and_singers=[]
    while True:   
        Index=random.randint(0,len(list_songs_and_singers)-1)
        MusicPlay(list_songs_and_singers[Index][0]()30)
        Input=CompleteVoiceAnalyse()
        if Input!=list_songs_and_singers[Index][1]:
            TTS("اشتباه بود","fa")
        elif Input=="بیرون":
            break
        else:
            TTS("درست بود","fa")
