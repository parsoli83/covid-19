from __rOBOT_fUNCTIONS__ import *
from datetime import datetime
import os
def reminder_drug():
    now = datetime.now()
    Time = now.strftime("%Y/%m/%d/%H/%M").split("/")
    time=int(Time[0])*365*24+int(Time[1])*30*24+int(Time[2])*24+int(Time[3])
    if os.path.isfile('REMINDERDRUGFILE.txt'):
        file=open("REMINDERDRUGFILE.txt","r")
        parsa=file.read().split("_")
        if len(parsa)==1:
            TTS("قرصی نداری راحت باش","fa")
        else:
            for ind in range(1,len(parsa)):
                drug=parsa[ind]
                drug=drug.split("/")
                Next=int(drug[2])+int(drug[1])
                if time>=Next:
                    TTS(drug[0])
    else:
        file=open("REMINDERDRUGFILE.txt","w")
        file.write("@")
    file.close()
def add_reminder_drug(name,hour):
    now = datetime.now()
    Time = now.strftime("%Y/%m/%d/%H/%M").split("/")
    time=int(Time[0])*365*24+int(Time[1])*30*24+int(Time[2])*24+int(Time[3])
    file=open("REMINDERDRUGFILE.txt", "r")
    file_=file.read().split("_")
    file_.remove("@")
    Text=name+"/"+str(hour)+"/"+str(time)
    file_.append(Text)
    file.close()
    filee=open("REMINDERDRUGFILE.txt", "w")
    final="@"
    for i in file_:
        final+="_"+i
    filee.write(final)
    filee.close()
def del_reminder_drug(name,hour=1):
    now = datetime.now()
    Time = now.strftime("%Y/%m/%d/%H/%M").split("/")
    time=int(Time[0])*365*24+int(Time[1])*30*24+int(Time[2])*24+int(Time[3])
    file=open("REMINDERDRUGFILE.txt", "r")
    file_=file.read().split("_")
    file_.remove("@")
    listi=None
    for l in file_:
        li=l.split("/")
        if li[0]==name:
            listi=li
    if listi!=None:
        listii=str(listi[0])+"/"+str(listi[1])+"/"+str(time)
        listi=str(listi[0])+"/"+str(listi[1])+"/"+str(listi[2])
        if hour==0:
            file_.remove(listi)
        else:
            file_[file_.index(listi)]=listii
    else:
        TTS("چنین دارویی وجود ندارد","fa")
    file.close()
    filee=open("REMINDERDRUGFILE.txt", "w")
    final="@"
    for i in file_:
        final+="_"+i   
    filee.write(final)
    filee.close()

