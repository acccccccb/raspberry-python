#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
import tkinter.messagebox as msg

import component.btn as btn
import control.cameraControl as camera

window = tkinter.Tk()
window.geometry("640x320")
window.title('raspberry control panel')

def takePhoto():
    print('开始录像')
    camera.takePhoto()
takePhoto()
btn1 = btn.creatBtn(window,"拍照","tan",takePhoto)

window.mainloop()