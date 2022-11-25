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

def Zero():
  for p in ZERO:
    GPIO.output(p, GPIO.HIGH)
    
def One():
  for p in ONE:
    GPIO.output(p, GPIO.HIGH)
    
def Two():
  for p in TWO:
    GPIO.output(p, GPIO.HIGH)
    
def Three():
  for p in THREE:
    GPIO.output(p, GPIO.HIGH)
    
def Four():
  for p in FOUR:
    GPIO.output(p, GPIO.HIGH)

def Five():
  for p in FIVE:
    GPIO.output(p, GPIO.HIGH)
    
def Six():
  for p in SIX:
    GPIO.output(p, GPIO.HIGH)
    
def Seven():
  for p in SEVEN:
    GPIO.output(p, GPIO.HIGH)
    
def Eight():
  for p in EIGHT:
    GPIO.output(p, GPIO.HIGH)
    
def Nine():
  for p in NINE:
    GPIO.output(p, GPIO.HIGH)
    
One()
sleep(3)
Six()
sleep(3)

GPIO.cleanup()
