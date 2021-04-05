#!/usr/bin/python3
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
from const import *
from lock import *
from buzzer import *

reader = SimpleMFRC522()

actual_tags = str(Path('tags.txt').read_text())

def rfid_listen():
  logging.debug("Listening for RFID")
  id, text = reader.read()
  return id



def rfid_write():
  logging.debug("Writing RFID")
  logging.info('Writing RFID')
  try:
        text = input('New data:')
        logging.debug("Now place your tag to write")
        reader.write(text)
        logging.debug("Written")
        logging.info("RFID Successfully Written")
  finally:
        GPIO.cleanup()


def capture_tag():
      input_tag_id = rfid_listen()
      while input_tag_id:
            buzzer_beep(1)
            if str(input_tag_id) in actual_tags:
                  logging.debug("Tag ID matches")
                  input_tag_id = ""
                  logging.debug("Unlock")
                  unlock_lock()
                  time.sleep(1)
                  capture_tag()
            else:
                  input_tag_id = ""
                  logging.debug("Tag ID does not match")
                  time.sleep(1)
                  capture_tag()

