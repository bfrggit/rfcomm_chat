#!/usr/bin/python

import time

from rf_listener import RFListener
from rf_writer import RFWriter

DEVICE = "/dev/rfcomm9"

listener = RFListener(dev = DEVICE)
listener.daemon = True
listener.start()

writer = RFWriter(dev = DEVICE)
writer.daemon = True
writer.start()

print "Started."
while True:
	time.sleep(1)
