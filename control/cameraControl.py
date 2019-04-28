#!/usr/bin/python
# -*- coding: UTF-8 -*-
from picamera import PiCamera
from time import sleep

def takePhoto():
    try:
        camera = PiCamera()
        # camera.resolution = (1440, 900)
        camera.start_preview()
    except KeyboardInterrupt:
        camera.stop_preview()
        camera.close()