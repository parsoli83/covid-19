#An introduction:
#its a function that will be used after covid_19 pandemic and
#it will be used toreciver patients in the hospital
#it works by getting the patients situation as input and then
#tell it what to do to get better
import numpy as np
from __rOBOT_fUNCTIONS__ import *
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
sport_teacher()
