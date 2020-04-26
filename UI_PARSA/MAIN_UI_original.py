from __rOBOT_fUNCTIONS__ import *
import time
from datetime import datetime
import random
import numpy as np
import os
#my libraries
from user_interface import *
from help import *
from supplementary import *
#l_functions=["سُرود","دآستآن","بآزی یآفتَن خآنَنده","بآزیِ مُهآسِبِه","تَشخیسِ کُرُنآ","بآزیِ بَلِه خِیرِ مَعکوس"
# ,"جُک گو","مُعآیِنِه خآب","تَجویز کُن","یآددآشت","یآددآشتِ دآرو","مُعَلِّمِ وَرزِش"]
##########################<<< main funtions >>>##########################                                                                                                         
def anthems():
  path="anthems >>>"
  list_en=np.array(["Poland","Russia","Soviet","United kingdom","Brazil","Canada","France","Germany","Iran","Italy"])
  list_fa=[["لهستان"],["روسیه"],["شوروی"],["اینگیلیس","انگلیس","انگلستان","بریتانیا"],["برزیل"],["کانادا"],["فرانسه"],["آلمان","المان"],["ایران"],["ایتالیا"]]
  def validator(name):
    print(path+"validator")
    for i in list_fa:
      for j in i:
        if j in name:
          return True
    return False
  def input_giver(): 
    print(path+"input_giver")                                                                                          
    TTS("نآمِ کِشوَر رآ بِگویید","fa")
    name=CompleteVoiceAnalyse()
    while validator(name)==False:
      if wanna_exit(name)==True:
        return False
      if wanna_help(name)==True:
        help()
        return False
      else:
        name=repeat_again()
    return name
  def anthem_player(name):
    print(path+"anthems_player")
    for i in list_fa:
      if name in i:
        MusicPlay(list_en[list_fa.index(i)]+"()text")
  def player(name):
    print(path+"player")
    if name==False:
        return 0
    if validator(name):
      anthem_player(name)
    else:
      name=input_giver()
      if name==False:
        return 0
      else:
        anthem_player(name)
  player(input_giver())
def story_player():
  path="story_player >>>"
  print(path)
  list_name=np.array(["آهوی لاغر","ابر کوچولو","برف و شادی","بشنو و باور نکن","بوسه ی راسو","جوجه های دارکوب","چکه آب،چکه باران","چه خانه ی زیبایی","خاله جان","خانه جدید خارپشت"])
  MusicPlay(random.choice(list_name)+"()compelete")
def find_singer():
  path="find_singer >>>"
  print(path)
  #you should put the list of singers and their songs here
  #it should be a 2-D list and like the below sentence
  #[[song name.mp3,singer]]
  list_songs_and_singers=np.array([["AronAfshar_1",["آرون افشار","افشار"]],["HamedBahram_1",["حامد بهرام","حامد","بهرام"]],["BehnamBani_1",["بهنام بانی","بهنام","بانی"]]])    
  def operator():  
    print(path+"operator")                                                                                                                                                         
    while True:                                                                                                                                            
      list_artist=random.choice(list_songs_and_singers)
      MusicPlay(list_artist[0]+"()30")
      TTS("نامِ خانَندِه چیست","fa")
      Input=CompleteVoiceAnalyse()
      l_=np.array(list_artist[1])
      con=False
      for i in l_:
        if i in Input:
          its_true()
          con=True
          continue
      if wanna_exit(Input):
        return 0
      if wanna_help(Input): 
        help()
        return 0
      if con==False:
        its_false()
  operator()
def calculating_game():
  path="calculating_game >>>"
  print(path)
  list_operators=["به علاوه","منهای","ضرب در"]
  level=1
  con=True
  while con==True:
    Text="حاصل"
    for i in range(level):
      Text+=" "+str(random.randint(1,9))+" "+random.choice(list_operators)
      Text+=" "+str(random.randint(1,9))
    TTS("شروع","fa")
    TTS(Text,"fa")
    Input=CompleteVoiceAnalyse()
    while numeric_input(Input)==False:
      if wanna_exit(Input):
        con=False
        return 0
      if wanna_help(Input):
        help()
        return 0
      else:
        Input=repeat_again()
    if calculater(Text)==int(Input):
      its_true()
      level+=1
    else:
      its_false()
def covid_19_diagonsis():
  score=0
  questions=["آیا لزر شدید دارید","آیا تب بالای ۳۸ درجه دارید","آیا در چند روز اخیر سرفه شدید دارید","آیا احساس گلودرد شدید دارید","آیا آسم و یا برونشیت دارید","آیا فشار خون شما بالاست","آیا دیابت داشته و با وجود تزریق انسولین هنوز عوارض دارید","آیا در شیمی درمانی به سر می برید","آیا کسی از نزدیکان شما به بیماری مبتلا شده","آیا تنگی نفس بسیار بالا دارید","آیا بینی شما کیپ است"]
  l_q=["یک","دو"]
  for question in questions:
    TTS(question,"fa")
    inp=CompleteVoiceAnalyse()
    while degree(inp)==False:
      if wanna_exit(inp):
        return 0
      if wanna_help(inp):
        help()
        return 0
      inp=repeat_again()
    score+=degree(inp)
  if score>=15:
    TTS("نیاز به بررسی دارید","fa")
  else:
    TTS("شما کاملا سالم هستید","fa")
def joke():
    jokes=np.array([
    '  دیدی درد نداشت؟        جمله نوستالژیک پدر و مادرها بعد آمپول زدن به بچه هاشون در حالی که بچه داره خون گریه میکنه     یعنی اون همه اشک ماله شوق بوده.',
     ' کار بابام از کولر گذشته       دیگه شبا بلند میشه میاد مودم رو خاموش میکنه!.'                                                                                      
    , ' دکمه روشن کنترلو 20 بار می زنی تلویزیون روشن نمی شه     عصبانی می شی، 2 بار پشت سر هم محکم فشار می دی روشن می شه دوباره خاموش می شه!'
    , ' دیگه به درجه ای از عرفان رسیدم که واسه خودم یه چیزی تعریف می کنم می خندم   تازه آخرش هم از خودم می پرسم جان من؟!'
    , ' یکی از محاسبه هایی که سریع انجام می دیم، محاسبه فاصله من و دادشم و خاهرم نسبت به آیفونه وقتی یکی زنگ درو می زنه!'
    , ' روزگارا که چنین سخت به من می گیری با خبر باش که خیلی داری سخت می گیری دیگه! مسخرشو درآوردی'                                                                               
    , ' از جلوی یه رستوران رد میشدم دیدم روی درش نوشته: لورل بیا هاردی برو!',                                                                     
     ' امروز دست خط خودمو بردم دارو خونه …        بهم دارو داد !'
    , ' یارو ميره تو صف نونوايي، شاطر نونوائی ميگه: نون تا اينجا بيشتر نميرسه، بقيه برن. ميگه: ببخشيد اگه ميشه جمعتر وايسين نون به ما هم برسه'
    , ' اگه میشد دانشمندا یه وسیله اختراع میکردند که از خروپوف برق تولید کنه الان بابام یه نیروگاه هسته ای محسوب می شد !.'
    , ' تا حالا دقت کردین کسایی که خروپف میکنن ،  زودتر خوابشون میبره !؟'                                                                                                                                                                                                                                                                          
    , ' رفتم دادگستری یارو میپرسه شکایت داشتید؟ گفتم پـَـــ نــه پـَـــ یه خورده برنج آوردم با ترازوی عدالت وزن کنم !.'
    , '  رفتم باغ وحش از نگهبانه میپرسم ببخشید آقا قفس شیرا کجاست ؟ میگه بازدید کننده ای پـَـــ نــه پـَـــ نه از اقوامشون هستم اینورا کاری داشتم گفتم سری بهشون بزنم',
     '  اومدم در یخچالو باز میکنم دنبال غذا مامانم میگه گشنته؟ پـَـــ نــه پـَـــ اومدم ببینم کی هی چراغ این تو رو خاموش روشن می کنه!.',
     ' یه بیماری هست اسم نداره اما نتیجه ش     نگهداشتن شیشه عطرها و اسپری های تموم شده ست !.',                                                                                                                                                         
     ' ﺑﻪ ﺑﻌﻀﯽ ﻫﺎ ﺑﺎﻳﺪ ﺑﮕﯽ :  ﺍﮔﻪ ﻭﺍﺳﻪ ﻫﻤﻪ ﻗﺎﻃﯽ ﭘﺎﺗﯽ ﻣﻴﮑﻨﯽ ، ﻭﺍﺳﻪ ﻣﺎ ﻫﻨﻮﺯ ﺗﺎﺗﯽ ﺗﺎﺗﯽ ﻣﻴﮑﻨﯽ !.',
     ' بدترین چیز اون خنده ی اجباری برای حفظ آبرو بعد از یه زمین خوردن وحشتناکه',
     ' بعضیا واسه همــه اقیانوس آرام هستن اما تا به ما میرسن میشن تنگهء هرمز!',
     ' فکر کنم رمز موفقیتمو ۳ بار اشتباه زدم قفل شده ',
     ' یه وقتایی لازمــه از گوشیمون بشنویم “مشترک مورد نظر آدم نمیباشد … لـــطفا قطع کنید”!',
     ' امسال نمایشگاه کتاب نرفتم ، خودم تو خونه سیب زمینی سرخ کردم خوردم !',
     ' زندگی مثل شطرنج میمونه ، البته تو که بچه ای برو منج بازی کن !',
     ' باهمه وجودم سرمو روشونه مهربون تو میذارم و یواشکی دماغمو با لباست پاک میکنم!!',
     ' خیلی دلم برات تنگ شده…اونقدر که از دوریت گریه ام میگره… اما وقتی قیافت یادم میاد خندم میگیره!!'
    , ' افتخار نکن که به اندازه تار موهات رفیق داری. وقتی محتاجشون میشی می فهمی که کچلی.',
     ' وقتی مو تو غذا باشه،فرقی نداره مژه ی دلبر باشه یا سیبیل اصغر آقا!',
     ' این دهه ۶٠یا که هی نسل سوخته نسل سوخته میکنن   فکر نکنن ما یادمون رفته ماه رمضوناشون تو زمستون بوده ..!',
     ' جمله ای که من هروقت یه آدم پولدار میبینم واسه آروم کردن خودم میگم: آرامشی که ما داریمو اونا ندارن!!'
    , ' میدونم یکی هست که تو دلش وِلولـس واسه خواستنــم فقط نمیدونم کجاست؟',                                                                                                                                                      
     ' بچه که بودم فکر میکردم زمان قدیم همه جا سیاه سفید بوده',
     ' بابام ﻣﯿﮕﻪ ﺍﻭﻝﮔﻮﺵ ﮐﻦ ﺑﺒﯿﻦ ﭼﯽ ﻣﯿﮕﻢ     ﺑﻌﺪ ﯾﺎ ﻗﺒﻮﻝ ﮐﻦﯾﺎ ﺑﺮﻭ ﻓﮑﺮﺍﺗﻮ ﮐﻦ ﺑﻌﺪ ﻗﺒﻮﻝ ﮐﻦ !',
     ' اومدم خونه به مامانم میگم گشنمه، میگه عزیزم نون هس ،تخم مرغ هس، روغنم هس،  برو هر چى دوس دارى درست کن بخور!'
    , ' دو ماهه دارم هر شش ساعت یه بار دوتا آنتی هیستامین میندازم تو جیبام    ولی بازم جیب ما به پول حساسیت داره!'
    , ' یه وختایی نمیرم دمه یخچال که پیشه من شرمنده نشه... خدا هیچ یخچالی رو شرمنده صاحبش نکنه.',                                                                                                                         
     ' دیگه کار از کلیپس گذشته برخی از دخترا در حال ساخت مسکن مهر رو سرشون هستند…!',
     '  اگه قرار باشه اون دنیا تو بهشت موسیقی های خوب گوش کنیم، فک کنم تو جهنم تتلو پخش کنن ',
     ' من حتی اگه بمیرم مامانم میاد سر قبرم میگه ببین بچه ی فلانی نصف توعه ولی زنده است ',
     ' پارسال با بابام دعوام شد بهش گفتم بالاخره یه روز از این خونه میرم الان یک ساله هر روز موقع شام و نهار میگه به به, شما که هنوز نرفتی.',
     '  دوستان نگران نباشید ویروس کرونا زود خراب میشه میمیره چون جنسش چینیه '                                                                                                            
    , '  انقدر که توی سایت ها ربات نبودنمو ثابت کردم توی زندگیم آدم بودنمو ثابت نکردم ',
     '  دلم برای روزایی که تو دبستان با بچه ها دعوامون میشد کیفشو برمیداشتم پرت کنم میگف ننننددداااازززقران توشه تنگ شده... ',
     ' هم عاشقتم , هم ازت متنفرم , میانگین که بگیری میبینی برام مهم نیستی !'                                                  
    , ' به سلامتی پنگوئن که یه ذره قد داره، اما بازم لاتی راه میره ….'
    , ' بزرگترین حرف های کینه توزانه با این جمله توجیه میشه : ” به خاطر خودت میگم “'
    , ' یه شلغمم نشدیم یکی کوفتمون کنه خوب شه…..!!'
    , ' یه کتابم نشدیم حداقل دوست مهربان بشیم !!', ' طنز بگو'
    ,' حیف نون به باباش میگه : پنکه خراب شدهباباش میگه : خوب معلومه پنج نفری زیرش میخوابین ، میخوای خراب نشه ؟!!',
    ' ه حیف نون میگن این خیابون کجا میره ؟میگه من ۴۰ ساله تو این خیابون زندگی میکنم تا حالا ندیدم جایی بره !', 
    ' احساسی که با خنده همراه است.'])                                                                                                                                       
    TTS(random.choice(jokes),"fa")
#in the name of the best programmer who programmed our minds and did it the best...
#it is a function that gets these arguments as input and then gives you data about sleep quality
#l_parameters=[total_sleep_time,deep_sleep,light_sleep,when_fell_asleep,when_woke_up]
#total_sleep_time should be shown by minute
#NOTE>>>time parameters should given as an intiger which displays time in minute like: 8:04>>>484 and ....
#i mean dont use AM or PM.......and dont use hours
#and the age of the patient
#returns the quality of sleep and advises what to do to sleep better
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
def reverse_True_and_False():
    list_questions=["آیا شما انسان هستید","یا بستنی داغ است","آیا زمین تخت است","آیا خورشید بنفش است","آیا جنگ خوب است","آیا فوتبال ورزش است","آیا قم کشور است","آیا فیل کوچک است","آیا ویروس بزرگ است","آیا رضا شاه وزیر بود","آیا شاهزاده وزیر است","آیا ماه ستاره است","آیا عراق شهر است","آیا پسر پدر وزیر پدرش است","آیا برج میلاد برج است","آیا شیر سیاه است","آیا سیاه روشن است","آیا خوبی بدی است","آیا اروپا کشور است","آیا بحرین بزرگ است","آیا آهن از پنبه سبک تر است"]
    key="nyyyynyyyyynyynyyyyyy"
    while True:
        Ind=random.randint(0,len(list_questions)-1)
        TTS(list_questions[Ind],"fa")
        iinput=CompleteVoiceAnalyse()
        while degree(iinput)==False:
            if wanna_exit(iinput):
                return 0
            if wanna_help(iinput):
              help()
              return 0
            iinput=repeat_again()
        if degree(iinput)==3:
            if key[Ind]=="y":
                its_true()
            else:
                its_false()
        elif degree(iinput)==1:
            if key[Ind]=="n":
                its_true()
            else:
                its_false()
def reminder():
  read_reminder()
  inp=tell_me()
  while True:
    if add_or_decrease(inp)==False:
      if wanna_exit(inp):
        return 0
      if wanna_help(inp):
        help()
        return 0
      inp=repeat_again()
    else:
      TTS("کآر رآ بِگویید","fa")
      job=CompleteVoiceAnalyse()
      if wanna_exit(job):
        return 0
      if wanna_help(job):
        help()
        return 0
      if add_or_decrease(inp)=="add":
        add_reminder(job)
      else:
        del_reminder(job)
def reminder_drug():
  read_reminder_drug()
  inp=tell_me()
  while True:
    if add_or_decrease(inp)==False:
      if wanna_exit(inp):
        return 0
      if wanna_help(inp):
        help()
        return 0
      inp=repeat_again()
    else:
      TTS("نامِ دآرو رآ بِگویید","fa")
      name=CompleteVoiceAnalyse()
      if wanna_exit(name):
        return 0
      if wanna_help(name):
        help()
        return 0
      TTS("هَر چَند سآعَت","fa")
      hour=CompleteVoiceAnalyse()
      if wanna_exit(hour):
        return 0
      if wanna_help(hour):
        help()
        return 0
      while numeric_input(hour)==False:
        if wanna_exit(hour):
          return 0
        if wanna_help(hour):
          help()
          return 0
        hour=repeat_again()
      if add_or_decrease(inp)=="add":
        add_reminder_drug(name,hour)
      else:
        del_reminder_drug(name,hour)
##########################<<< the operator >>>##########################
def main_operator(voice):
  ################INTRUDOCTION################
  #THIS THE PART THET OPERATES ALL THE CODE
  #IT GIVES THE COMMAND AS INPUT AND IF IT IS ABOUT FUNCTIONS OR
  #HELP OR.......IT WILL WORK
  #OTHERWISE RETURN FALSE
  ################################
  #l_functions=["سُرود","دآستآن","بآزی یآفتَن خآنَنده","بآزیِ مُهآسِبِه","تَشخیسِ کُرُنآ","بآزیِ بَلِه خِیرِ مَعکوس"
  # ,"جُک گو","مُعآیِنِه خآب","تَجویز کُن","یآددآشت","یآددآشتِ دآرو","مُعَلِّمِ وَرزِش"]
  #>>>>these are for specifying the keywords
  #>> casual functions
  l_anthem_keywords=np.array([
    "سرود","ملی"
  ])
  l_story_keywords=np.array([
    "داستان","قصه","غصه","حکایت"
  ])
  l_joker_keywords=np.array([
    "جک","لطیفه","جوک"
  ])
  l_reminder_keywords=np.array([
    "یادداشت","دفتر","یاد"
  ])
  #>>related to game functions
  l_find_singer_keywords=np.array([
    "خاننده","اهنگ","خواننده"
  ])
  l_calculation_game_keywords=np.array([
    "محاسبه","ماشین","حساب","بازی"
  ])
  l_reverse_t_f_keywords=np.array([
    "بله","خیر","معکوس"
  ])
  #>>related to covid_19 and hospital
  l_corona_dignose_keywords=np.array([
    "کرونا","کورونا","کووید","کوید","تشخیص"
  ])
  l_sleep_manager_keywords=np.array([
    "خاب","خواب","استراحت"
  ])
  l_prescription_keywords=np.array([
    "نسخه","تجویز","پیشنهاد","نوسخه"
  ])
  l_drug_reminder_keywords=np.array([
    "دارو","قرص","قورص","قورس"
  ])
  if wanna_exit(voice):
    return 0
  if wanna_help(voice):
    help()
    return 0
  if find_if_in_or_not(l_anthem_keywords,voice):
    anthems()
  if find_if_in_or_not(l_story_keywords,voice):
    story_player()
  if find_if_in_or_not(l_joker_keywords,voice):

    joke()
  if find_if_in_or_not(l_reminder_keywords,voice):
    reminder()
  if find_if_in_or_not(l_find_singer_keywords,voice):
    find_singer()
  if find_if_in_or_not(l_calculation_game_keywords,voice):
    calculating_game()
  if find_if_in_or_not(l_reverse_t_f_keywords,voice):
    reverse_True_and_False()
  if find_if_in_or_not(l_corona_dignose_keywords,voice):
    covid_19_diagonsis()
#  if find_if_in_or_not(l_sleep_manager_keywords,voice):>>>neesds connection to mi band which isnt available at the moment
#    mi_sleep_assistant()
#  if find_if_in_or_not(l_prescription_keywords,voice):
#    pres()
  if find_if_in_or_not(l_drug_reminder_keywords,voice):
    reminder_drug()
#  if find_if_in_or_not(l_sport_teacher_keywords,voice):
#    sport_teacher()  
while True:
  main_operator(CompleteVoiceAnalyse())

            
