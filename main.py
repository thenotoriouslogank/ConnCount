import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

A = 17
B = 27
C = 22
class Display:
  def __init__(self, digit: int, segments: list):
    self.digit = digit
    self.segments = segments
D = 23
E = 24
F = 25
G = 19
DP = 6

class Display:
  def __init__(self, digit: int, segments: list):
    self.digit = digit
    self.segments = segments

ZERO = Display(0, [A, B, C, D, E, F])
ONE = Display(1, [B, C])
TWO = Display(2, [A, B, D, E, G])
THREE = Display(3, [A, B, C, D, G])
FOUR = Display(4, [B, C, F, G])
FIVE = Display(5, [A, C, D, F, G])
SIX = Display(6, [A, C, D, E, F, G])
SEVEN = Display(7, [A, B, C])
EIGHT = Display(8, [A, B, C, D, E, F, G])
NINE = Display(9, [A, B, C, F, G])
ALL = Display(10, [A, B, C, D, E, F, G, DP])
DIGITS = [ALL, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
MyNum = 0

def Prep():
  GPIO.setup(ALL.segments, GPIO.OUT)

def TestMe():
  print(ALL.segments)

def LED():
  for i in DIGITS:
    print(i.digit)

#def Check():
#  if ZERO.digit == MyNum:
#    print('ZERO')
#  else:
#    print('Somethig done got fuckered.')
#

Prep()
TestMe()
LED()
#Check()
#Zero()
#sleep(1)
#Clear()
#One()
#sleep(1)
#Clear()
#Two()
#sleep(1)
#Clear()
#Three()
#sleep(1)
#Clear()
#Four()
#sleep(1)
#Clear()
#Five()
#sleep(1)
#Clear()
#Six()
#sleep(1)
#Clear()
#Seven()
#sleep(1)
#Clear()
#Eight()
#sleep(1)
#Clear()
#Nine()
#sleep(1)
#Clear()
#All()
#sleep(1)
#Clear()
#print("Done.")
sleep(10)
GPIO.cleanup()
