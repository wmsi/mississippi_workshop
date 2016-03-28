import pico 
import RPi.GPIO as GPIO

# Sets numbering system
GPIO.setmode(GPIO.BCM)

# Set pin 21 for digital output
led = 21
GPIO.setup(led, GPIO.OUT)

# Set the initial state to off
GPIO.output(led, 0)

# Function called by javascript to set state
def setState(state):
	GPIO.output(led, state)
