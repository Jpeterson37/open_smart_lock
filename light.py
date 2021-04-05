from const import *

def light_bar_on():
    logging.debug("Light Bar On")
    light_out.on()

def light_bar_off():
    logging.debug("Light Bar Off")
    light_out.off()

def light_bar_blink(times):
    # logging.debug("Light Bar Blink " + times + " Times")
    light_out.blink(on_time=.3, off_time=.3, n=times, background=True)
