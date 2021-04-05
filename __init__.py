#!/usr/bin/python3
from multiprocessing import Process
from const import *
from pin import *
from light import *
from lock import *
#from rfid import *
from shutdown import *
from program import *


logging.debug('Starting')

def setup():
    logging.debug('Begin setup')
    lock_current_state()
    logging.debug('End setup')
    return True

def program():
    if program_button.value == 1:
        programing()
    elif program_button.value == 0:
        program_write()
        


if __name__=='__main__':
    if setup():
        program_button.when_pressed = programing
        program_button.when_released = program_write
        Lock_State_Process = Process(target = lock_state_change())
        Lock_State_Process.start()
        PIN_Process = Process(target = user_PIN())
        PIN_Process.start()
        RFID_Process = Process(target = capture_tag())
        RFID_Process.start()
        #MQTT_Process = Process(target = lock_state_change())
        #MQTT_Process.start()
        #Shutdown_Process = Process(target = shutdown_proccess())
        #Shutdown_Process.start()
    
    pause()