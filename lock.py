#!/usr/bin/env python
from const import lock_state_switch, lock_out
from light import *
import time

def lock_current_state():
    lock_state = "unknown"
    if lock_state_switch.value == 1:
        lock_state = "locked"
        logging.debug("Lock is " + lock_state)
        light_bar_off()
    elif lock_state_switch.value == 0:
        lock_state = "unlocked"
        logging.debug("Lock is " + lock_state)
        light_bar_on()
    return lock_state

def unlock_lock():
    logging.debug("Unlocking Lock")
    i = 0
    while not (lock_current_state() == "unlocked"):
        lock_out.blink(on_time=0.5, off_time=.5, n=1, background=True)
        time.sleep(1)
        if i == 3:
            break
        i += 1
    else:
        return True
    

def lock_state_change():
    logging.debug("Lock state process started")
    lock_state_switch.when_pressed = lock_current_state
    lock_state_switch.when_released = lock_current_state


