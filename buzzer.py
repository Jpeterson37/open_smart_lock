#!/usr/bin/python3
from const import *

def buzzer_on():
    logging.debug("Buzzer On")
    buzzer_out.on()

def buzzer_off():
    logging.debug("Buzzer Off")
    buzzer_out.off()

def buzzer_beep(times):
    buzzer_out.beep(on_time=.3, off_time=.3, n=times, background=True)

buzzer_on()
pause()