from __rOBOT_fUNCTIONS__ import *
import time
import random
import numpy as np
##########################<<< "ui_parsa" FUNCTIONS >>>##########################
#INTRODUCTION:
#these functions are built to let the main functions communicate in a better and 
#more organized way
def couldnt_understand():
  List=np.array(["متاسفانه متوجهِ منظورتون نِمیشم","متاسفانه متوجه نَشدم","شرمنده متوجه منظورتون نِمیشم","شرمنده متوجهِ نشدم","من دارم یاد میگیرم و متوجهِ منظورتون نِمیشم","متاسفانه نفهمیدم"])
  TTS(random.choice(List),"fa")                                                                                                                                                                       
def repeat_again():
  List=np.array(["لُطفاً تِکرار کُنید","یِک بآر دیگَر بِگویید","دُبارِه تِکرآر کُنید"])
  TTS(random.choice(List),"fa")
  name=CompleteVoiceAnalyse()
  return name
def wanna_exit(text):
  List=np.array(["خروج","خارج","بیرون","تمام","توقف","متوقف"])
  if text in List:
    return True
  for i in List:
    if i in text:
      return True
  return False
def wanna_help(text):
  List=np.array(["کمک","راهنما","سوال","سُال"])
  if text in List:
    return True
  for i in List:
    if i in text:
      return True
  return False
def its_true():
  List=np.array([
    "دُرُستِه",
    "بَلِه",
    "آفَرین"
  ])
  TTS(random.choice(List),"fa")
def its_false():
  List=np.array([
    "قَلَتِه",
    "نادُرُست",
    "خِیر"
  ])
  TTS(random.choice(List),"fa")
##########################<<< help center >>>##########################
def help():
  #tells you how the help works
  def help_introducer():
    TTS("جَهَت اِتِّلآع اَز اَنوآع وَ تِعداد خَدََمآت بَگویید خَدَمآت وَ دَر جَهَت اِتِّلآع اَز نَهوِه کآر هَر یِک نآم آن خِدمَت رآ بِگویید","fa")
  #tells about the functions and 
  def functions_introducer():                                                                                                                                                                               
    l_functions=np.array(["سُرود","دآستآن","بآزی یآفتَن خآنَنده","بآزیِ مُهآسِبِه","تَشخیسِ کُرُنآ","بآزیِ بَلِه خِیرِ مَعکوس","جُک گو","مُعآیِنِه خآب","تَجویز کُن","یآددآشت","یآددآشتِ دآرو","مُعَلِّمِ وَرزِش"])
    for i in l_functions:                                                                                                                                                                                                                                                                  
      TTS(i,"fa")
  ######>>>>>>>>>>>>>>>>help of functions>>>>>>>>>>>>>>>>#####
  #this is the help for anthems
  def help_anthems():
    TTS("این خِدمَت بَرآیِ خآندَنِ سُرود مِلّی کِشوَر هآست وَ نَحوِه کار بآ آن بِه این شِکل اَست کِه اِسمِ کِشوَرِ مُرِدِ نَظَر را می گویید و سُرود پَخش می شَوَداین خِدمَت بَرای اَفزایِشِ روحیه اَست","fa")
  l_main_words=np.array(["این خِدمَت بَرآیِ","وَ نَهوِه کآرِ آن بِه این شِکل اَست کِه","هَدَفِ این خِدمَت"])#its for making the descriptions more organized
  #this is the help for story player
  def help_story():
    l=np.array(["پَخشِ دآستان اَست","یِک دآستآن زیبآ رآ پَخش می کُنَد","اَفزآیِشِ روهیِه کودَکآن اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")
      TTS(l[i],"fa")
  #this is the help for find singer game
  def help_find_singer():
    l=np.array(["یِک مُسابِقِه جَزّاب اَست","بَخشی اَز یِک آهَنگ پَخش می شَوَد وَ شُمآ بآیَد خآنَندِه رآ حَدس بِزَنید","سَرگَرمی بیمآران اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")
      TTS(l[i],"fa")
  #this is the help for calculation game
  def help_calculation_game():
    l=np.array(["یِک مُسابِقِه جَزّاب اَست","یَک عَبآرَت ریآضی بَرآیِ شُمآ پَخش می شَوَد وَ شُمآ بآیَد جَوآب آن رآ بِگویید عِبآرَت ها مَرحَلِه بِه مَرحَلِه سَخت می شَوَند","سَرگَرمی بیمآران اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for covid 19 diagnosis
  def help_corona_diagnose():
    l=np.array(["یَک مُعآیِنِه پِزِشکی اَست","چَند سُآل اَز شُمآ پُرسیدِه می شَوَد وَ شُمآ جَواب می دَهید وَ دَر نَهایَت نَتیجِه مُعآیِنِه اِعلآم می شَوَد","تَشخیصِ بیمآرآن اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for reverse true or false game
  def help_reverse_T_F():
    l=np.array(["یِک مُسابِقِه جَزّاب اَست","یِک جُملِه اِعلآم می شَوَد و شُمآ بآید بَرعَکس پآسُخ دَهید","سَرگَرمی بیمآران اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for joker
  def help_joker():
    l=np.array(["یِک سَرگَرمی اَست","رُبآت جُک می گویَد","سَرگَرمی بیمآران اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for sleep manager
  def help_sleep_manager():
    l=np.array(["یَک مُعآیِنِه پِزِشکی اَست","خآبِ شُما بَررَسی می شَوَد وَ پیشنَهآد هآیی بَرآیِ بِهبودِ آن می دهَم","بِبودِ خآبِ بیمآرآن اَست"])    
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for prescription function
  def help_prescription():
    l=np.array(["یَک مُعآیِنِه پِزِشکی اَست","وَضعیَتِ سَلامَتِ شُمآ بآ پُرسیدَنِ چَند سُآل مُشَخَّس می شَوَد وَ شُمآ بآیَد بِه هَر سُآل جَوآبی بِین سِفر تا دَه بِدَهید دَر نَهآیَت پیشنَهاد هآیی بَرآی بِبود شُمآ می دَهَم","بِهبودِ سَریع تَر بیمآرآن اَست"])    
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for reminder function
  def help_reminder():
    l=np.array(["کُمَک بِه یآدآوَری چیز هآست","بَعد اَز گُفتَنِ یآددآشت کآرهآ جَهَت اِضافِه کَردَن بِگویید جَدید وَ سِپَس کآر رآ بِگویید وَ جَهَت کَم کَردَن بِگویید کَم وَ سِپَس کآر رآ بِگویید","کُمَک بِه بیمآرآن اَست"])    
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for reminder drug
  def help_reminder_drug():
    l=np.array(["کُمَک بِه یآدآوَری دآرو هآست","این خِدمَت بِه سورَتِ خُدکآر دَر زَمآن مُعَیَّن دآرو هآی آن زَمان دآرو هآ رآ میخآنَد بَعد اَز گُفتَن دآرو جَهَت اِضافِه کَردَن بِگویید جَدید و جَهَت هَزفِ دآرو بِگویید کَم","بِهبودِ سَریع تَر بیمآرآن اَست"])
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #this is the help for sport teacher func
  def help_sport_teacher():
    l=np.array([
      "یَک مُعآیِنِه پِزِشکی اَست"
      ,"رُبآت اُز شُمآ چَند سُآل می پُرسَد وَ دَر آخَر پیشنَهاد هآی وَرزِشی می دَهَد"
      ,"بِهبودِ سَریع تَر بیمآرآن اَست"
    ])
    for i in range(3):
      TTS(l_main_words[i],"fa")                                                                                                                                             
      TTS(l[i],"fa")
  #>>>this is the operator of the help functions
  def help_operator():
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
      "محاسبه","ماشین","حساب"
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
    l_sport_teacher_keywords=np.array([
      "ورزش","مربی","معلم","حرکت"
    ])
    def find_if_in_or_not(List,text):
      for i in List:
        if i in text:
          return True
      return False
    TTS(random.choice(np.array(["چِه کُمَکی میخآهید","چِه سُآلی دآرید","چِه کآری میتَوانَم بُکُنَم","چِه مُشکِلی دآرید"])),"fa")
    voice=CompleteVoiceAnalyse()
    if wanna_exit(voice):
      return 0
    #the help for help
    if "راهنما" in voice:
      help_introducer()
    #talks about functions
    if "خدمات" in voice:
      functions_introducer()
    #describes the functions
    if find_if_in_or_not(l_anthem_keywords,voice):
      help_anthems()
    if find_if_in_or_not(l_story_keywords,voice):
      help_story()
    if find_if_in_or_not(l_joker_keywords,voice):
      help_joker()
    if find_if_in_or_not(l_reminder_keywords,voice):
      help_reminder()
    if find_if_in_or_not(l_find_singer_keywords,voice):
      help_find_singer()
    if find_if_in_or_not(l_calculation_game_keywords,voice):
      help_calculation_game
    if find_if_in_or_not(l_reverse_t_f_keywords,voice):
      help_reverse_T_F()
    if find_if_in_or_not(l_corona_dignose_keywords,voice):
      help_corona_diagnose()
    if find_if_in_or_not(l_sleep_manager_keywords,voice):
      help_sleep_manager()
    if find_if_in_or_not(l_prescription_keywords,voice):
      help_prescription()
    if find_if_in_or_not(l_drug_reminder_keywords,voice):
      help_reminder_drug()
    if find_if_in_or_not(l_sport_teacher_keywords,voice):
      help_sport_teacher()
  help_operator()
##########################<<<functions to help(suppliementary)>>>##########################
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
##########################<<< main funtions >>>##########################                                                                                                         
def anthems(name=False):
  list_en=np.array(["Poland","Russia","Soviet","United kingdom","Brazil","Canada","France","Germany","Iran","Italy"])
  list_fa=np.array([["لهستان"],["روسیه"],["شوروی"],["اینگیلیس","انگلیس","انگلستان","بریتانیا"],["برزیل"],["کانادا"],["فرانسه"],["آلمان","المان"],["ایران"],["ایتالیا"]])
  def input_giver():                                                                                           
    TTS("نآمِ کِشوَر رآ بِگویید","fa")
    name=CompleteVoiceAnalyse()
    while validator(name)==False:
      if wanna_exit(name)==True:
        return False
      if wanna_help(name)==True:
        help()
      else:
        name=repeat_again()
  def validator(name):
    for i in list_fa:
      if name in i:
        return True
    return False
  def anthem_player(name):
    for i in list_fa:
      if name in i:
        MusicPlay(list_en[list_fa.index(i)]+"()text")
  def player(name):
    if validator(name):
      anthem_player(name)
    else:
      name=input_giver()
      if name==False:
        return 0
      else:
        anthem_player(name)
  player(name)
def story_player():
  list_name=np.array(["آهوی لاغر","ابر کوچولو","برف و شادی","بشنو و باور نکن","بوسه ی راسو","جوجه های دارکوب","چکه آب،چکه باران","چه خانه ی زیبایی","خاله جان","خانه جدید خارپشت"])
  MusicPlay(random.choice(list_name)+"()compelete")
def find_singer():
  #you should put the list of singers and their songs here
  #it should be a 2-D list and like the below sentence
  #[[song name.mp3,singer]]
  list_songs_and_singers=np.array([["AronAfshar_1",["آرون افشار","افشار"]],["HamedBahram_1",["حامد بهرام","حامد","بهرام"]],["BehnamBani_1",["بهنام بانی","بهنام","بانی"]]])    
  def operator():                                                                                                                                                           
    while True:                                                                                                                                            
      list_artist=random.choice(list_songs_and_singers)
      MusicPlay(random.choice(list_artist[0])+"()30")
      TTS("نامِ خانَندِه چیست","fa")
      Input=CompleteVoiceAnalyse()
      l_=np.array(list_artist[1])
      con=False
      for i in l_:
        if i in Input:
          its_true()
          con=True
      if wanna_exit(Input):
        return 0
      if wanna_help(Input):
        help()
        return 0
      if con==False:
        its_false()
  operator()
def calculating_game():
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
    while Is_numeric(Input)==False:
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
    