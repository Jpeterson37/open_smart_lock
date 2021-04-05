from const import *

def buzzer_on():
    logging.debug("Buzzer On")
    light_out.on()

def buzzer_off():
    logging.debug("Buzzer Off")
    light_out.off()

def buzzer_blink(times):
    buzzer_out.beep(on_time=.3, off_time=.3, n=times, background=True)
