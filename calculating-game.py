import __rOBOT_fUNCTIONS__
import random
import time
def Is_numeric(Text):
    if Text.isnumeric()==True:
        return True
    elif Text[0]=="-":
        TEXT=Text.replace("-","")
        return TEXT.isnumeric()
    else:
        return False
def calculater(text):
    #analizing part
    l_operations=[]
    l_names=[["تقسیم","/"],["ضرب","*"],["جمع","هوالع","علاوه","مجموع","+"],["منفی","منهای","-"]]
    #,["توان"],["رادیکال"]
    l_numbers=[]
    text=text.split()
    for item in text:
        if Is_numeric(item)==True:
            l_numbers.append(int(item))
        for lis in l_names:
            if item in lis:
                l_operations.append(lis[-1])
    l_full=[]
    for i in range(len(l_operations)):
        l_full.append(l_numbers[i])
        l_full.append(l_operations[i])
    l_full.append(l_numbers[-1])
    while "*" in l_full or "/" in l_full:
        ind_1=100
        ind_2=100
        if "*" in l_full:
            ind_1=l_full.index("*")
        if "/" in l_full:
            ind_2=l_full.index("/")
        ind=min(ind_1,ind_2)
        num_1=l_full[ind-1]
        num_2=l_full[ind+1]
        sum=0
        if l_full[ind]=="*":
            sum=int(num_1*num_2)
        else:
            sum=int(num_1/num_2)
        l_full.pop(ind)
        l_full.pop(ind)
        l_full.pop(ind-1)
        l_full.insert(ind-1,sum)
    while "+" in l_full or "-" in l_full:
        ind_1=100
        ind_2=100
        if "+" in l_full:
            ind_1=l_full.index("+")
        if "-" in l_full:
            ind_2=l_full.index("-")
        ind=min(ind_1,ind_2)
        num_1=l_full[ind-1]
        num_2=l_full[ind+1]
        sum=0
        if l_full[ind]=="+":
            sum=int(num_1+num_2)
        else:
            sum=int(num_1-num_2)
        l_full.pop(ind)
        l_full.pop(ind)
        l_full.pop(ind-1)
        l_full.insert(ind-1,sum)
    return l_full[0]
def calculating_game():
    list_operators=["به علاوه","منهای","ضرب در"]
    level=1
    con=True
    while con==True:
        Text="حاصل"
        for i in range(level):
            Text+=" "+str(random.randint(1,9))+" "+random.choice(list_operators)
        Text+=" "+str(random.randint(1,9))
        __rOBOT_fUNCTIONS__.TTS("شروع","fa")
        __rOBOT_fUNCTIONS__.TTS(Text,"fa")
        Input=__rOBOT_fUNCTIONS__.CompleteVoiceAnalyse()
        while Is_numeric(Input)==False:
            if Input=="تمام":
                con=False
                return 0
            else:
                __rOBOT_fUNCTIONS__.TTS("دوباره بگو")
                Input=__rOBOT_fUNCTIONS__.CompleteVoiceAnalyse()
        if calculater(Text)==int(Input):
            __rOBOT_fUNCTIONS__.TTS("درسته","fa")
            level+=1
        else:
            __rOBOT_fUNCTIONS__.TTS("غلطه","fa")
calculating_game()