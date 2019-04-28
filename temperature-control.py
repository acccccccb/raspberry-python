import os
import RPi.GPIO as GPIO
import time

fs = 14
redLed = 26
blueLed = 4


count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(fs,GPIO.OUT)
GPIO.setup(redLed,GPIO.OUT)
GPIO.setup(blueLed,GPIO.OUT)


def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

def pilotLamp(led,action):
	c = 0
	if action == 'on':
		#while (c==0):
		GPIO.output(led,GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(led,GPIO.LOW)
		time.sleep(5)
	else:
		c=1
		GPIO.output(led,GPIO.LOW)

try:
	while ( count == 0 ) :
		CPU_temp = getCPUtemperature()
		if float(CPU_temp) >= 55 :
			GPIO.output(fs,GPIO.HIGH)
			pilotLamp(redLed,'on')
                        pilotLamp(blueLed,'off')
			print(getCPUtemperature())
			print("Fan power on")
			
	
		elif float(CPU_temp) <= 45 :
			GPIO.output(fs,GPIO.LOW)
			pilotLamp(redLed,'off')
			pilotLamp(blueLed,'on')
			print("Fan power off")
			
		else :
			print("CPU Temperature:" + CPU_temp)
			pilotLamp(redLed,'off')
			pilotLamp(blueLed,'on')

			
			
		time.sleep(10)

except KeyboardInterrupt:
	GPIO.output(redLed,GPIO.HIGH)
	GPIO.output(blueLed,GPIO.HIGH)
	GPIO.output(fs,GPIO.HIGH)
	GPIO.cleanup()
