import os
import time
# Return CPU temperature as a character string                                     
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
count = 0
while count == 0 :
	print(getCPUtemperature())
	time.sleep(1)
