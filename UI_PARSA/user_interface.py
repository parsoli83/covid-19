from __rOBOT_fUNCTIONS__ import *
import time
from datetime import datetime
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
def tell_me():
  l=np.array([
    "بِفَرمآیید",
    "بگویید",
    "میشِنَوَم",
  ])
  TTS(random.choice(l),"fa")
  return CompleteVoiceAnalyse()