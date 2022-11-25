import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

A = 17
B = 27
C = 22
D = 23
E = 24
F = 25
G = 19
DP = 6

ZERO = [A, B, C, D, E, F]
ONE = [B, C]
TWO = [A, B, D, E, G]
THREE = [A, B, C, D, G]
FOUR = [B, C, F, G]
FIVE = [A, C, D, F, G]
SIX = [A, C, D, E, F, G]
SEVEN = [A, B, C]
EIGHT = [A, B, C, D, E, F, G]
NINE = [A, B, C, F, G]
ALL = [A, B, C, D, E, F, G, DP]

def Prep():
  for segments in ALL:
    GPIO.setup(segments, GPIO.OUT)

""" 
GPIO.setup(A, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)
GPIO.setup(C, GPIO.OUT)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(F, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(DP, GPIO.OUT)
 """
def Zero():
  for p in ZERO:
    GPIO.output(p, GPIO.LOW)
    
def One():
  for p in ONE:
    GPIO.output(p, GPIO.LOW)
    
def Two():
  for p in TWO:
    GPIO.output(p, GPIO.LOW)
    
def Three():
  for p in THREE:
    GPIO.output(p, GPIO.LOW)
    
def Four():
  for p in FOUR:
    GPIO.output(p, GPIO.LOW)

def Five():
  for p in FIVE:
    GPIO.output(p, GPIO.LOW)
    
def Six():
  for p in SIX:
    GPIO.output(p, GPIO.LOW)
    
def Seven():
  for p in SEVEN:
    GPIO.output(p, GPIO.LOW)
    
def Eight():
  for p in EIGHT:
    GPIO.output(p, GPIO.LOW)
    
def Nine():
  for p in NINE:
    GPIO.output(p, GPIO.LOW)

def All():
  for p in ALL:
    GPIO.output(p, GPIO.LOW)

def Clear():
  for p in ALL:
    GPIO.output(p, GPIO.HIGH)

Prep()
Zero()
sleep(1)
Clear()
One()
sleep(1)
Clear()
Two()
sleep(1)
Clear()
Three()
sleep(1)
Clear()
Four()
sleep(1)
Clear()
Five()
sleep(1)
Clear()
Six()
sleep(1)
Clear()
Seven()
sleep(1)
Clear()
Eight()
sleep(1)
Clear()
Nine()
sleep(1)
Clear()
All()
sleep(1)
Clear()
print("Done.")
sleep(10)
GPIO.cleanup()
