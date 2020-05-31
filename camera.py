#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
import tkinter.messagebox as msg

import component.btn as btn

from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)



window = tkinter.Tk()
window.geometry("640x320")
window.title('raspberry control panel')

def takePhoto():
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')
    

def stopCamera():
    print('stop录像')

btn1 = btn.creatBtn(window,"拍照","tan",takePhoto)
btn1 = btn.creatBtn(window,"stop拍照","tan",stopCamera)
window.mainloop()
