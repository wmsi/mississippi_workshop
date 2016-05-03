import pico
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def getState(pin):
	GPIO.setup(pin,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	state = GPIO.input(pin)
	print "State is " + str(state)
	return state
