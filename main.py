import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

A = 17
GPIO.setup(A, GPIO.OUT)

B = 27
GPIO.setup(B, GPIO.OUT)

C = 22
GPIO.setup(C, GPIO.OUT)

D = 23
GPIO.setup(D, GPIO.OUT)

E = 24
GPIO.setup(E, GPIO.OUT)

F = 25
GPIO.setup(F, GPIO.OUT)

G = 19
GPIO.setup(G, GPIO.OUT)

DP = 6
GPIO.setup(DP, GPIO.OUT)

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
