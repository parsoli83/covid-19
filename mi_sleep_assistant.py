#in the name of the best programmer who programmed our minds and did it the best...
#it is a function that gets these arguments as input and then gives you data about sleep quality
#l_parameters=[total_sleep_time,deep_sleep,light_sleep,when_fell_asleep,when_woke_up]
#total_sleep_time should be shown by minute
#NOTE>>>time parameters should given as an intiger which displays time in minute like: 8:04>>>484 and ....
#i mean dont use AM or PM.......and dont use hours
#and the age of the patient
#returns the quality of sleep and advises what to do to sleep better
import os
#import matplotlib.pyplot as plt
from __rOBOT_fUNCTIONS__ import *
def mi_sleep_assistant(age,total_sleep_time,deep_sleep,light_sleep,when_fell_asleep,when_woke_up):
    #l_sleep_and_age=a list that shows the sleep neede in any age
    #structure=[[starting age,oldest age,sleep needed]]
    l_sleep_and_age=[[0,1,720],[2,6,540],[7,12,480],[13,50,420],[50,1000,360]]
    l_prescriptions=[]
    if when_fell_asleep<600:
        l_prescriptions.append("زودتَر بِخابید")
    for i in l_sleep_and_age:
        if age>=i[0] and age<=i[1]:
            if total_sleep_time<=i[2]:
                l_prescriptions.append("بیشتَر بِخابید")
    if deep_sleep<90:
        #it was what i wanted to extend but now its okay too
        l_prescriptions.append("خآبِ اَمیق نَدآرید")
    if len(l_prescriptions)==0:
        l_prescriptions.append("خآبِ شُمآ عآلی اَست")
    for i in l_prescriptions:
        TTS(i,"fa")
mi_sleep_assistant(15,480,60,420,1,481)