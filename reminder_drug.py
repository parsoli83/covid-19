from datetime import datetime
import os
def reminder_drug():
    now = datetime.now()
    Time = now.strftime("%Y/%m/%d").split("/")
    time=int(Time[0])*365*24+int(Time[0])*30*24+int(Time[0])*24   
    if os.path.isfile('REMINDERDRUGFILE.txt'):
        file=open("REMINDERDRUGFILE.txt","r")
        parsa=file.read().split("_")
        if len(parsa)==1:
            print("قرصی نداری راحت باش")
        else:
            for ind in range(1,len(parsa)):
                drug=parsa[ind]
                drug=drug.split("/")
                Next=int(drug[2])+int(drug[1])
                if time>=Next:
                    print(drug[0])
    else:
        file=open("REMINDERDRUGFILE.txt","w")
        file.write("@")
    file.close()
def add_reminder_drug(name,hour):
    now = datetime.now()
    Time = now.strftime("%Y/%m/%d").split("/")
    time=int(Time[0])*365*24+int(Time[0])*30*24+int(Time[0])*24
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
    Time = now.strftime("%Y/%m/%d").split("/")
    time=int(Time[0])*365*24+int(Time[0])*30*24+int(Time[0])*24
    file=open("REMINDERDRUGFILE.txt", "r")
    file_=file.read().split("_")
    file_.remove("@")
    listi=None
    for l in file_:
        l=l.split("/")
        print(l)
        if l[0]==name:
            listi=l
    print(listi)
    if listi!=None:
        if hour==0:
            file_.remove(listi)
        else:
            listi[2]=time
            listi=str(listi[0])+"/"+str(listi[1])+"/"+str(listi[2])
    else:
        print("چنین دارویی وجود ندارد")
    file.close()
    filee=open("REMINDERDRUGFILE.txt", "w")
    final="@"
    for i in file_:
        final+="_"+i
    filee.write(final)
    filee.close()

