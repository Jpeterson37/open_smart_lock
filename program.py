#!/usr/bin/env python
from const import *
from light import *
import time



new_input_pin = ""
new_input_rfid = ""

def program_PIN1_pressed():
    light_bar_blink(1)
    capture_new_pin("1")

def program_PIN2_pressed():
    light_bar_blink(1)
    capture_new_pin("2")

def program_PIN3_pressed():
    light_bar_blink(1)
    capture_new_pin("3")

def program_PIN4_pressed():
    light_bar_blink(1)
    capture_new_pin("4")

def capture_new_pin(input):
    global new_input_pin
    new_input_pin += input
    print(new_input_pin)

def programing():
    print("Programing")
    light_bar_blink(2)
    PIN1.when_pressed = program_PIN1_pressed
    PIN2.when_pressed = program_PIN2_pressed
    PIN3.when_pressed = program_PIN3_pressed
    PIN4.when_pressed = program_PIN4_pressed

def validate_new_pin():
    new_pin = str(Path('pin.txt').read_text().rstrip('\n'))
    if new_input_pin == new_pin:
        print("PIN Successfully Changed")
        time.sleep(2)
        light_bar_on()
    else:
        print("PIN Set Error")
        light_bar_blink(10)

def program_write():
    if new_input_pin:
        print("Writting new PIN: " + new_input_pin)
        light_bar_blink(3)
        Path('pin.txt').write_text(new_input_pin)
        if validate_new_pin():
            return True
    elif new_input_rfid:
        print("Writting new RFID tag: " + new_input_rfid)
        light_bar_blink(4)
        Path('rfid.txt').write_text('my text')
    else:
        print("No new vlues")
        light_bar_on()
    
    
