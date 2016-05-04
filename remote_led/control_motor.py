import pico
import ev3dev.ev3 as ev3
import time

#define motor
m = ev3.LargeMotor('outA')

#define the run time for the motor
runTime = 3000

#function called by javascript to set state
def setState(state):
	power = int(state)*75
	m.run_timed(time_sp=runTime,duty_cycle_sp=power)
	print(state)
