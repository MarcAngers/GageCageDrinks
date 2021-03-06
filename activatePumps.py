import RPi.GPIO as gpio
import time
SHOT_TIME = 17

def setup():
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)

	# setup pumps:
	gpio.setup(2, gpio.OUT)
	gpio.setup(3, gpio.OUT)
	gpio.setup(4, gpio.OUT)
	gpio.setup(5, gpio.OUT)
	gpio.setup(6, gpio.OUT)
	gpio.setup(7, gpio.OUT)
	gpio.setup(8, gpio.OUT)
	gpio.setup(9, gpio.OUT)

	# setup mixer:
	gpio.setup(27, gpio.OUT)

	# turn on cpu fan
	gpio.setup(20, gpio.OUT)
	gpio.output(20, gpio.HIGH)

def activatePumps(pumpArray):
	for i in range(8):
		if pumpArray[i] > 0:
			gpio.output((i+2), gpio.HIGH)

	while(any(pump > 0 for pump in pumpArray)):
		time.sleep(SHOT_TIME)
		for i in range(8):
			if pumpArray[i] <= 1:
				gpio.output((i+2), gpio.LOW)
			pumpArray[i] -= 1
	
	# mix the ingredients!
	gpio.output(27, gpio.HIGH)
	time.sleep(8)
	gpio.output(27, gpio.LOW)

	return "Success!"

def cleanup():
	gpio.output(20, gpio.LOW)
	gpio.cleanup()
