#!/usr/bin/env python
import sys
sys.path.append("/home/homeassistant/lib/pyenergenie/src/")

import time
import energenie

APP_DELAY = 1

# Devices that use the standard Energenie house code
all_sockets = energenie.Devices.ENER002(0)
socket1     = energenie.Devices.ENER002(1)
socket2     = energenie.Devices.ENER002(2)
socket3     = energenie.Devices.ENER002(3)
socket4     = energenie.Devices.ENER002(4)

# A device that uses a custom house code (e.g. learnt from a hand controller)
socket5     = energenie.Devices.ENER002((0x1234, 1))

# A MiHome device that we know the address of from a previous capture
socket6     = energenie.Devices.MIHO005(0x68b)

sockets     = [all_sockets, socket1, socket2, socket3, socket4, socket5, socket6]


if __name__ == "__main__":
    energenie.init()
    socket_no = 2
    try:
        print("socket %d ON" % socket_no)
        sockets[socket_no].turn_on()
        time.sleep(APP_DELAY)
        print("socket %d OFF" % socket_no)
        sockets[socket_no].turn_off()
        time.sleep(APP_DELAY)
    finally:
        energenie.finished()
