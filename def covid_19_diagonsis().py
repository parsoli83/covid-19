from __rOBOT_fUNCTIONS__ import *
def degree(answer):
    list_degrees=[["نه","اصلا","ابدا","هیچ","خیر"],["تقریبا","کمی","یکم"],["آره","بله","بلی","دقیقا"]]
    con=False
    for i in list_degrees:
        for item in i:
            if item in answer:
                con=True
                return list_degrees.index(i)+1
    return con
def covid_19_diagonsis():
    score=0
    questions=["آیا لزر شدید دارید","آیا تب بالای ۳۸ درجه دارید","آیا در چند روز اخیر سرفه شدید دارید","آیا احساس گلودرد شدید دارید","آیا آسم و یا برونشیت دارید","آیا فشار خون شما بالاست","آیا دیابت داشته و با وجود تزریق انسولین هنوز عوارض دارید","آیا در شیمی درمانی به سر می برید","آیا کسی از نزدیکان شما به بیماری مبتلا شده","آیا تنگی نفس بسیار بالا دارید","آیا بینی شما کیپ است"]
    for question in questions:
        TTS(question,"fa")
        inp=CompleteVoiceAnalyse()
        while degree(inp)==False:
            TTS("لُطفً دُبآرِ جَوآب دَهید","fa")
            inp=CompleteVoiceAnalyse()
        score+=degree(inp)
    if score>=15:
        TTS("نیاز به بررسی دارید","fa")
    else:
        TTS("شما کاملا سالم هستید","fa")
covid_19_diagonsis()
