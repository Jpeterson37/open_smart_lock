#!/usr/bin/python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from const import *
from lock import *
from buzzer import *

reader = SimpleMFRC522()

actual_tags = str(Path('tags.txt').read_text())

def rfid_listen():
  print("Listening for RFID")
  id, text = reader.read()
  print(id)
  print(text)
  return id



def rfid_write():
  print("Writing RFID")
  logging.info('Writing RFID')
  try:
        text = input('New data:')
        print("Now place your tag to write")
        reader.write(text)
        print("Written")
        logging.info("RFID Successfully Written")
  finally:
        GPIO.cleanup()


def capture_tag():
      input_tag_id = rfid_listen()
      while input_tag_id:
            buzzer_blink(1)
            logging.debug(input_tag_id)
            logging.debug(actual_tags)
            if input_tag_id in actual_tags:
                  logging.debug("Tag ID matches")
                  input_tag_id = ""
                  print("Unlock")
                  #unlock_lock()
                  capture_tag()
            else:
                  input_tag_id = ""
                  logging.debug("Tag ID does not match")
                  capture_tag()

capture_tag()