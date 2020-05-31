import RPi.GPIO as GPIO
import time
import sys

LED = 18
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
action = sys.argv;
print(action[1]);
try:
        if (action[1]=='1'):
            GPIO.output(LED, GPIO.LOW)
        else:
            GPIO.output(LED, GPIO.HIGH)

except KeyboardInterrupt:
	GPIO.output(LED,GPIO.HIGH)
	GPIO.cleanup()

