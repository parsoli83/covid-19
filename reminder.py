from __rOBOT_fUNCTIONS__ import *
def reminder () :
    if os.path.isfile('REMINDERFILE.txt'):
        file=open("REMINDERFILE.txt","r")
        parsa=file.read().split("_")
        if len(parsa)==1:
            TTS("کاری نداری راحت باش","fa")
        else:
            for i in range(1,len(parsa)):
                TTS(parsa[i],"fa")
    else:
        file=open("REMINDERFILE.txt","w")
        file.write("@")
    file.close()
def add_reminder(text):
    file=open("REMINDERFILE.txt", "r")
    file_=file.read().split("_")
    file_.remove("@")
    file_.append(text)
    file.close()
    filee=open("REMINDERFILE.txt", "w")
    final="@"
    for i in file_:
        final+="_"+i
    filee.write(final)
    filee.close()
def del_reminder(text):
    file=open("REMINDERFILE.txt", "r")
    file_=file.read().split("_")
    file_.remove("@")
    if text in file_:
        file_.remove(text)
    else:
        TTS("چنین کاری وجود ندارد","fa")
    file.close()
    filee=open("REMINDERFILE.txt", "w")
    final="@"
    for i in file_:
        final+="_"+i
    filee.write(final)
    filee.close()
