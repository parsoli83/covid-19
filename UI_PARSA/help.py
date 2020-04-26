from __rOBOT_fUNCTIONS__ import *
import time
from datetime import datetime
import random
import numpy as np
#my libraries
from user_interface import *
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
    l=np.array(["کُمَک بِه یآدآوَری چیز هآست","بَعد اَز گُفتَنِ یآددآشت کآرهآ پَخش می شَوَد جَهَت اِضافِه کَردَن بِگویید جَدید وَ سِپَس کآر رآ بِگویید وَ جَهَت کَم کَردَن بِگویید کَم وَ سِپَس کآر رآ بِگویید","کُمَک بِه بیمآرآن اَست"])    
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
      help_calculation_game()
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