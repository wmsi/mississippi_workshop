import pico 
from pico import PicoApp
import RPi.GPIO as GPIO
import time

red = 18
yellow = 19
green = 20

def setModeAll():
	GPIO.setmode(GPIO.BCM)
	for x in range (18,21):
		GPIO.setup(x,GPIO.OUT)

# Function called by javascript to set state
@pico.expose()
def setStateRed(state=0):
	setModeAll()
	GPIO.output(red, state)
	GPIO.output(yellow,0)
	GPIO.output(green,0)
	print "Red LED toggled, yes sir"
	
@pico.expose()
def setStateYellow(state=0):
	setModeAll()
	GPIO.output(yellow, state)
	GPIO.output(red,0)
	GPIO.output(green,0)
	print "Yellow LED toggled, yes sir"
	
@pico.expose()
def setStateGreen(state=0):
	setModeAll()
	GPIO.output(green, state)
	GPIO.output(red,0)
	GPIO.output(yellow,0)
	print "Green LED toggled, yes sir"



app=PicoApp()
app.register_module(__name__)
