#!/usr/bin/env python
from const import *

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from log import *

reader = SimpleMFRC522()

def rfid_read():
  print("Reading RFID")
  logging.info('Reading RFID')
  try:
      id, text = reader.read()
      print(id)
      print(text)
      logging.info("Got ID value: " + str(id))
      logging.info("Got Text value: " + text)
  finally:
      GPIO.cleanup()



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