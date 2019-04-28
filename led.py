import RPi.GPIO as GPIO
import time

LED = 4	#blue led
#LED = 26	#red led
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

try:

	while ( count < 3 ) :
		GPIO.output(LED, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(LED, GPIO.LOW)
		time.sleep(3)
		#count = count + 1

except KeyboardInterrupt:
	GPIO.output(LED,GPIO.HIGH)
	GPIO.cleanup()
