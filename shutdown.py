#!/usr/bin/python3
from gpiozero import Button
from subprocess import check_call
from const import *

def shutdown():
    check_call(['sudo', 'poweroff'])

def shutdown_proccess():
    shutdown_btn = Button(shutdown_button, hold_time=2)
    shutdown_btn.when_held = shutdown