#!/usr/bin/env python
import time
from energenie import encoder, radio

INNER_TIMES = 16
OUTER_TIMES = 1
APP_DELAY = 1

HOUSE_ADDRESS = None

ALL_ON     = encoder.build_switch_msg(True,                    house_address=HOUSE_ADDRESS)
ONE_ON     = encoder.build_switch_msg(True,  device_address=1, house_address=HOUSE_ADDRESS)
TWO_ON     = encoder.build_switch_msg(True,  device_address=2, house_address=HOUSE_ADDRESS)
THREE_ON   = encoder.build_switch_msg(True,  device_address=3, house_address=HOUSE_ADDRESS)
FOUR_ON    = encoder.build_switch_msg(True,  device_address=4, house_address=HOUSE_ADDRESS)
ON_MSGS    = [ALL_ON, ONE_ON, TWO_ON, THREE_ON, FOUR_ON]

ALL_OFF    = encoder.build_switch_msg(False,                   house_address=HOUSE_ADDRESS)
ONE_OFF    = encoder.build_switch_msg(False, device_address=1, house_address=HOUSE_ADDRESS)
TWO_OFF    = encoder.build_switch_msg(False, device_address=2, house_address=HOUSE_ADDRESS)
THREE_OFF  = encoder.build_switch_msg(False, device_address=3, house_address=HOUSE_ADDRESS)
FOUR_OFF   = encoder.build_switch_msg(False, device_address=4, house_address=HOUSE_ADDRESS)
OFF_MSGS   = [ALL_OFF, ONE_OFF, TWO_OFF, THREE_OFF, FOUR_OFF]

radio.transmit(ON_MSGS[1], OUTER_TIMES, INNER_TIMES)
time.sleep(APP_DELAY)
radio.transmit(OFF_MSGS[1], OUTER_TIMES, INNER_TIMES)