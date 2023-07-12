import time
SHOT_TIME = 17

def setup():
	return

def activatePumps(pumpArray):
	while(any(pump > 0 for pump in pumpArray)):
		time.sleep(SHOT_TIME)
		for i in range(8):
			pumpArray[i] -= 1
	
	time.sleep(8)

	return "Success!"

def cleanup():
	return
