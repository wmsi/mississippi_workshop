import pico 
import pigpio

pi = pigpio.pi()

pin = "21"
pi.set_mode(pin, pipio.OUTPUT)

def setState(state):
	pi.write(pin, state)

def getState(pin):
	state = pi.read(pin)
	return "The state of pin " + str(pin) + " is " + str(state)
	
