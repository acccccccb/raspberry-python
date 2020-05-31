import smbus
import time

bus = smbus.SMBus(1)
address = 0x27
text = bus.read_byte_data(address,0x58)
#print(text)import smbus
import logx
import logging
import os
import time
import socket
import datetime
                                  
BUS = smbus.SMBus(1)
LCD_ADDR = 0x27
BLEN = 1 #turn on/off background light
def turn_light(key):
	global BLEN
	BLEN = key
	if key ==1 :
		BUS.write_byte(LCD_ADDR ,0x08)
		logging.info('LCD executed turn on BLight')
	else:
		BUS.write_byte(LCD_ADDR ,0x00)
		logging.info('LCD executed turn off BLight')

def write_word(addr, data):
	global BLEN
	temp = data
	if BLEN == 1:
		temp |= 0x08
	else:
		temp &= 0xF7
	BUS.write_byte(addr ,temp)

def send_command(comm):
	# Send bit7-4 firstly
	buf = comm & 0xF0
	buf |= 0x04               # RS = 0, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)
	
	# Send bit3-0 secondly
	buf = (comm & 0x0F) << 4
	buf |= 0x04               # RS = 0, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)

def send_data(data):
	# Send bit7-4 firstly
	buf = data & 0xF0
	buf |= 0x05               # RS = 1, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)
	
	# Send bit3-0 secondly
	buf = (data & 0x0F) << 4
	buf |= 0x05               # RS = 1, RW = 0, EN = 1
	write_word(LCD_ADDR ,buf)
	time.sleep(0.002)
	buf &= 0xFB               # Make EN = 0
	write_word(LCD_ADDR ,buf)

def init_lcd():
	try:
		send_command(0x33) # Must initialize to 8-line mode at first
		time.sleep(0.005)
		send_command(0x32) # Then initialize to 4-line mode
		time.sleep(0.005)
		send_command(0x28) # 2 Lines & 5*7 dots
		time.sleep(0.005)
		send_command(0x0C) # Enable display without cursor
		time.sleep(0.005)
		send_command(0x01) # Clear Screen
		logging.info('LCD init over')
		BUS.write_byte(LCD_ADDR ,0x08)
		logging.info('LCD turning on BLight')
	except:
		return False
	else:
		return True

def clear_lcd():
	send_command(0x01) # Clear Screen

def print_lcd(x, y, str):
	if x < 0:
		x = 0
	if x > 15:
		x = 15
	if y <0:
		y = 0
	if y > 1:
		y = 1

	# Move cursor
	addr = 0x80 + 0x40 * y + x
	send_command(addr)
	
	for chr in str:
		send_data(ord(chr))

def getIp():
    hostname = socket.gethostname()
    htname = socket.getfqdn(hostname)
#    ip = socket.gethostbyname(hostname)
#    addr = socket.getaddrinfo(hostname,None)
    
    try:
        s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        realIp = s.getsockname()[0]
    finally:
        s.close()
    print(realIp)
    return realIp

def getTime():
    time = datetime.datetime.now()
    return time.strftime("%H:%M:%S")

def clearLcd():
    print_lcd(0, 0, '                    ')
    print_lcd(0, 1, '                    ')
# Return CPU temperature as a character string   
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))


try:
    if __name__ == '__main__':
        init_lcd()
	print_lcd(0,0,"start success")
	print_lcd(0,1,"wait 30s")
	time.sleep(30)
	clearLcd()
	print_lcd(0,0,getIp())
        count = 0
        while count == 0 :
            #print(getCPUtemperature())
            #clearLcd()
            #print_lcd(0, 0, getIp())
            print_lcd(10, 1, getCPUtemperature() + " C")
            print_lcd(0, 1, getTime())
            time.sleep(0.1)
except KeyboardInterrupt:
        clearLcd()


