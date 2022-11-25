import RPi.GPIO as GPIO
from ping import ping
from extract import GetTotal
from time import sleep

A = 17
B = 27
C = 22
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

def Prep():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(ALL.segments, GPIO.OUT)
  fp = open('ip', 'x')
  fp.close()

def LED():
  for i in DIGITS:
    if i.digit == extract.total:
      GPIO.output(i.segments, GPIO.LOW)

Prep()
ping()
GetTotal()
LED()
sleep(10)
GPIO.cleanup()