import pico
import ev3dev.ev3 as ev3

def getState(channel):
	channelStr = 'in'+ str(channel)
	ls=ev3.ColorSensor(channelStr)
	value = ls.value()
	return value
