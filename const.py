from gpiozero import Button, DigitalOutputDevice, LED
import time
from log import *
from pathlib import Path
from signal import pause


global program_button, shutdown_button, lock_state_switch, bouncetime, PIN1, PIN2, PIN3, PIN4, lock_out, light_out

bouncetime = 0.001
#Input Devices
program_button = Button(6)
shutdown_button = Button(5)
lock_state_switch = Button(12,bounce_time=bouncetime)


#PIN
PIN1, PIN2, PIN3, PIN4 = Button(27), Button(18), Button(17), Button(4)

#Output Devices
lock_out = DigitalOutputDevice(22)
light_out = LED(23)