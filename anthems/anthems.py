import __rOBOT_fUNCTIONS__
from random import randint
def anthems(name="nothing"):
    list_en=["Poland","Russia","Soviet","United kingdom","Brazil","Canada","France","Germany","Iran","Italy"]
    list_fa=[["لهستان"],["روسیه"],["شوروی"],["اینگیلیس","انگلیس","انگلستان","بریتانیا"],["برزیل"],["کانادا"],["فرانسه"],["آلمان","المان"],["ایران"],["ایتالیا"]]
    while name not in list_fa or name!="خروج":
        Index=random.randint(0,9)
        ــrOBOT_fUNCTIONS__.TTS(random.choice(["متاسفانه متوجهِ منظورتون نِمیشم","متاسفانه متوجه نَشدم","شرمنده متوجه منظورتون نِمیشم","شرمنده متوجهِ نشدم","من دارم یاد میگیرم و متوجهِ منظورتون نِمیشم","متاسفانه نفهمیدم"]),"fa")
        name=__rOBOT_fUNCTIONS__.CompleteVoiceAnalyse()
    else:
        for i in list_fa:
            if name in i:
                MusicPlay(list_en[list_fa.index(name)]+()+text)
                return 0
anthems(__rOBOT_fUNCTIONS__.CompleteVoiceAnalyse())