from __rOBOT_fUNCTIONS__ import *
def reverse_True_and_False():
    list_questions=["آیا شما انسان هستید","یا بستنی داغ است","آیا زمین تخت است","آیا خورشید بنفش است","آیا جنگ خوب است","آیا فوتبال ورزش است","آیا قم کشور است","آیا فیل کوچک است","آیا ویروس بزرگ است","آیا رضا شاه وزیر بود","آیا شاهزاده وزیر است","آیا ماه ستاره است","آیا عراق شهر است","آیا پسر پدر وزیر پدرش است","آیا برج میلاد برج است","آیا شیر سیاه است","آیا سیاه روشن است","آیا خوبی بدی است","آیا اروپا کشور است","آیا بحرین بزرگ است","آیا آهن از پنبه سبک تر است"]
    key="nyyyynyyyyynyynyyyyyy"
    while True:
        Ind=random.randint(0,len(list_questions)-1)
        TTS(list_questions[Ind],"fa")
        iinput=CompleteVoiceAnalyse()
        if iinput=="بله" or iinput=="آره":
            if key[Ind]=="y":
                TTS("درسته","fa")
            else:
                TTS("غلطه","fa")
        elif iinput=="خیر" or iinput=="نه":
            if key[Ind]=="n":
                TTS("درسته","fa")
            else:
                TTS("غلطه","fa")
        elif iinput=="خروج":
            break
        else:
            TTS("دوباره بگویید","fa")
            continue
reverse_True_and_False()
