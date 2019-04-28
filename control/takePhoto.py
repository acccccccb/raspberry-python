#!/usr/bin/python
# -*- coding: UTF-8 -*-
from picamera import PiCamera
from time import sleep

def takePhoto():
    camera = PiCamera()
    camera.start_preview()
    sleep(10)
    camera.stop_preview()