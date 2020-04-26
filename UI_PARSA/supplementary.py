from __rOBOT_fUNCTIONS__ import *
import time
from datetime import datetime
import random
import numpy as np
#my libraries
from user_interface import *
from help import *
##########################<<<functions to help(suppliementary)>>>##########################
#this function returns a degeree based on what the customer says
#its used in covis_19_diagnosis functions
def score_finder(l_symp):
    """
    this is how i measure the health_index:
    fever: abs(your fever-37)*100 eg >>> 39.5==250
    tiredness: a number between 0 and 10 *10
    cough: a number between 0 and 10 *10
    difficulty in breathing: a number between 0 and 10 *10
    sneeze: a number between 0 and 10 *10
    then add all the above scores
    """
    #l_symp:[fever,tiredness,cough,difficulty in breathing,sneeze]
    score=0
    score+=abs(l_symp[0]-37)*100+l_symp[1]*10+l_symp[2]*10+l_symp[3]*10+l_symp[4]*10
    return score
def degree(answer):
    list_degrees=[
      ["نه","اصلا","ابدا","هیچ","خیر"]
      ,["تقریبا","کمی","یکم"]
      ,["آره","بله","بلی","دقیقا"]
    ]
    con=False
    for i in list_degrees:
        for item in i:
            if item in answer:
                con=True
                return list_degrees.index(i)+1
    return con
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
def Is_numeric(Text):
    if Text.isnumeric()==True:
        return True
    elif Text[0]=="-":
        TEXT=Text.replace("-","")
        return TEXT.isnumeric()
    else:
        return False
#DESCRIPTION:
#this func is made to handle persian numeric inputs
#when you call it, it uses "CompleteVoiceAnalyse()" as voice analyzer
#then if the word was a numeric_string it will change its format to int and returns it
#otherwise it will return False
############################################################
#ATTENTION:IT CAN JUST CHANGE NUMBERS TYPE FROM 0 TO 999
############################################################
def numeric_input(persian_number_string):
  #i use this list to find out if the word is a number or not
  l_persian_number_strings=np.array([
    #zero:
    [
      ["صفر","صفرم","هیچ"]
    ],
    #1_digit numbers:
    [
      ["یک","اول","نخست"],
      ["دو","دوم"],
      ["سه","سوم"],
      ["چهار","چار","چهارم"],
      ["پنج","پنجم"],
      ["شش","شیش","شیشم","ششم"],
      ["هفتم","هفت"],
      ["هشت","هشتم"],
      ["نه","نهم"]
    ],
    #2_digit numbers >>> 11 to 19:
    [
      ["یازده","یازدهم"],
      ["دوازده","دوازدهم"],
      ["سیزده","سیزدهم"],
      ["چارده","چهارده","چاردهم","چهاردهم"],
      ["پانزده","پونزده","پانزدهم","پونزدهم"],
      ["شانزده","شونزده","شانزدهم","شونزدهم"],
      ["هفدهم","هیوده","هیفدهم","هوده","هیودهم","هفده","هیفده","هودهم"],
      ["هیجده","هیجدهم","ه‍‍جده","هجدهم"],
      ["نونزده","نانزده","نوزده","نونزدهم","نانزدهم","نوزدهم"]
    ],
    #2_digit numbers >>> 10 to 90:
    [
      ["ده","دهم"],
      ["بیست","بیستم"],
      ["سی","سیم"],
      ["چهل","چهلم"],
      ["پنجاه","پنجاهم"],
      ["شست","شستم"],
      ["پنجاه","پنجاهم"],
      ["شست","شستم"],
      ["هفتاد","هفتادم"],
      ["هشتاد","هشتادم"],
      ["نود","نودم"]
    ],
    #3_digit numbers:
    [
      ["صد","صدم","یکصد","یک صد","یک صدم","یکصدم"],
      ["دویست","دویستم"],
      ["سیصد","سیصدم"],
      ["چهارصد","چارصد","چهارصدم","چارصدم"],
      ["پانصد","پونصد","پانصدم","پونصدم"],
      ["ششصد","شیشصد","ششصدم","شیشصدم"],
      ["هفتصد","هفتصدم","هفصد","هفصدم"],
      ["هشصد","هشتصد","هشصدم","هشتصدم"],
      ["نهصد","نهصدم"]
    ]
  ])
  #the processing part
  if type(persian_number_string)==int:
    return persian_number_string
  else:
    persian_number_string=persian_number_string.split()
    while "و" in persian_number_string:
      persian_number_string.remove("و")
    for i in range(len(persian_number_string)):
      sample=persian_number_string[i]
      while "ُ" in persian_number_string[i]:
        sample.remove("ُ")
      persian_number_string[i]=sample
  full_number=0
  for num in persian_number_string:
    con=False
    #check if its zero
    for i in l_persian_number_strings[0][0]:
      if num==i:
        con=True
        full_number+=0
    #check if its a number from 1 to 9
    for digit in l_persian_number_strings[1]:
      if num in digit:
        full_number+=(l_persian_number_strings[1].index(digit)+1)
    #check if its a number from 11 to 19
    for digit in l_persian_number_strings[2]:
      if num in digit:
        full_number+=(l_persian_number_strings[2].index(digit)+1)+10
    #check the greater ranges
    for dimension in range(3,len(l_persian_number_strings)):
      for digit in l_persian_number_strings[dimension]:
        if num in digit:
          full_number+=(l_persian_number_strings[dimension].index(digit)+1)*10**(dimension-2)
  if full_number==0 and con==False:
    return False
  else:
    return full_number
def add_or_decrease(inp):
  l_add=np.array([
    "جدید"
    ,"اضافه"
    ,"نو"
    ,"ازافه"
    ,"افزایش"
    ,"زیاد"
  ])
  l_decrease=np.array([
    "کم",
    "کاهش",
    "حذف",
    "حزف",
    "لغو",
    "لقو"
  ])
  for i in l_add:
    if i in inp:
      return "add"
  for i in l_decrease:
    if i in inp:
      return "decrease"
  return False
def read_reminder () :
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
def read_reminder_drug():
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
def find_if_in_or_not(List,text):
      for i in List:
        if i in text:
          return True
      return False
def find_whether_in_or_not(l,item,Index):#to help me find things in 2-d lists and arrays
    for i in l:
        if i[Index]==item:
            return True
    return False  
def input_manager_BETA():
    ######################################################
    #ATTENTION:it works on terminal beacause of problems with input of numbers
    ######################################################
    #it gets these factors as input:
    #l_factors=[age,illness_type,symptops_with_degrees]
    #illness types are deseases(like virus and bacteria),fraction,venenation,pain and other
    #symptomps_with_degree are the symptomps in the list below and their degree from 1 to 10:
    #list symptoms:
    arr_places=np.array(
        ["سر","گردن","کمر","گلو","ریه","شکم","دست","پا","زانو","مچ","other"]
    ) #the parts of pains
    arr_problems=np.array(
        ["بدندرد","سردرد","اسهال","ابریزش","تب","کوفتگی","خون"] 
    )#the kind of pains
    #illness_types:
    arr_illness_types=np.array(["deseases","fraction","venenation","pain","other"])
    #they are kept in this structure:
    #[[symptomp,degree],[symptomp,degree],...]
    l_case=np.array([None,None,None])
    age=int(input("tell your age:"))
    l_case[0]=age
    l_symp=[]
    print("illness_types are:")
    print(arr_illness_types)
    illness_type=input()
    while illness_type not in arr_illness_types:
        print("couldnt understand or not in list")
        illness_type=input()
    l_case[1]=illness_type
    print("choos your symptomps:")
    print(arr_places)
    print(arr_problems)
    print("ends by typing -1")
    i=1
    fucking_text="symp"+str(i)+":"
    Input=input(fucking_text).split(" ")
    while True:
        i+=1
        if Input[0]=="-1" or Input[0]=="-۱":
            break
        elif (Input[0] in arr_places or Input[0] in arr_problems) and len(Input)>1:
            l_symp.append([Input[0],int(Input[1])])
        else:
            print("couldnt understand or not in list")
        fucking_text="symp"+str(i)+":"
        Input=input(fucking_text).split(" ")
    l_case[2]=l_symp
    return l_case
def input_manager_sport_teacher():
    #it gets these factors as input:
    #l_factors=[age,illness_type,symptops_with_degrees]
    #illness types are deseases(like virus and bacteria),fraction,venenation,pain and other
    #symptomps_with_degree are the symptomps in the list below and their degree from 1 to 10:
    #list symptoms:
    arr_places=np.array(
        ["سر","گردن","کمر","گلو","ریه","شکم","دست","پا","زانو","مچ","other"]
    ) #the parts of pains
    arr_problems=np.array(
        ["بدندرد","سردرد","اسهال","ابریزش","تب","کوفتگی","خون"] 
    )#the kind of pains
    #illness_types:
    arr_illness_types=np.array(["deseases","fraction","venenation","pain","other"])
    #they are kept in this structure:
    #[[symptomp,degree],[symptomp,degree],...]
    l_case=np.array([None,None,None])
    TTS("چَند سآل دآرید","fa")
    inp=CompleteVoiceAnalyse()
    while numeric_input(inp)==False:
      if wanna_exit(inp):
        return 0
      if wanna_help(inp):
        help()
        return 0
      inp=repeat_again()
    l_case[0]=numeric_input(inp)
    
def sport_teacher():
    l_case=input_manager_BETA()
    l_symp=l_case[2]
    l_warmup=np.array(["پیاده روی","حرکات هوازی","حرکات تعادلی","حرکات کششی",])
    l_specialistic=np.array(["جلو بازو","بارفیکس","دو درجا","چرخش سر","چرخش کمر","چرخش مچ","کشش دست"])
    l_when0k=np.array(["پروانه","دراز نشست"])
    l_final=["استراحت"]
    """
    arr_places=np.array(
        ["سر","گردن","کمر","گلو","ریه","شکم","دست","پا","زانو","مچ","other"]
    ) #the parts of pains
    arr_problems=np.array(
        ["بدندرد","سردرد","اسهال","ابریزش","تب","کوفتگی","خون"] 
    )#the kind of pains
    """
    patient_condition=True #it is here to measure whether it can do hard sports or not
    worst_symp=None
    for symp in l_symp:
        if symp[1]>7:
            patient_condition=False
    if patient_condition==True:
        if len(l_symp)<3:
            l_final.append("حرکات هوازی")
            l_final.append("حرکات تعادلی")
            l_final.append("پروانه")
            l_final.append("دراز نشست")
        if len(l_symp)<5:
            l_final.append("حرکات کششی")
            if find_whether_in_or_not(l_symp,"پا",0)==False and find_whether_in_or_not(l_symp,"زانو",0)==False:
                l_final.append(l_warmup[0])
                l_final.append("دو درجا")
            if find_whether_in_or_not(l_symp,"کمر",0)==False:
                l_final.append("چرخش کمر")
            if find_whether_in_or_not(l_symp,"مچ",0)==True:
                l_final.append("چرخش مچ")
            if find_whether_in_or_not(l_symp,"دست",0)==True:
                l_final.append("کشش دست")
            if find_whether_in_or_not(l_symp,"گردن",0)==True:
                l_final.append("چرخش سر")
            if find_whether_in_or_not(l_symp,"گلو",0)==True or find_whether_in_or_not(l_symp,"ریه",0)==True:
                l_final=["استراحت","نوشیدنی گرم"]          
    for i in l_final:
        TTS(i,"fa")