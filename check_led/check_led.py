import pico
import RPi.GPIO as GPIO

# Sets numbering system
GPIO.setmode(GPIO.BCM)

def getState(pin):
	state = GPIO.input(pin)
	return "LED at pin" + str(pin) + "is state" + str(state)
