#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
def creatBtn(_target,_text,_color,_action):
    btn = tkinter.Button(_target, text=_text,bg=_color, command=_action)
    btn.pack()
    return btn
