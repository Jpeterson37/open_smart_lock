#!/usr/bin/python3
from gpiozero import Button
from func_timeout import func_timeout, FunctionTimedOut
from const import *
from lock import *
from buzzer import *

actual_pin = str(Path('pin.txt').read_text().rstrip('\n'))
input_pin = ""


def PIN1_pressed():
    buzzer_beep(1)
    capture_pin("1")

def PIN2_pressed():
    buzzer_beep(1)
    capture_pin("2")

def PIN3_pressed():
    buzzer_beep(1)
    capture_pin("3")

def PIN4_pressed():
    buzzer_beep(1)
    capture_pin("4")

def capture_pin(input):
    global input_pin
    input_pin += input
    if len(input_pin) == len(actual_pin):
        logging.debug(input_pin)
        logging.debug(actual_pin)
        if input_pin == actual_pin:
            logging.debug("PIN matches")
            #trigger unlock
            input_pin = ""
            unlock_lock()
        else:
            input_pin = ""
            logging.debug("Incorrect PIN")
        return True

def user_PIN():
    logging.debug("PIN function started")
    PIN1.when_pressed = PIN1_pressed
    PIN2.when_pressed = PIN2_pressed
    PIN3.when_pressed = PIN3_pressed
    PIN4.when_pressed = PIN4_pressed