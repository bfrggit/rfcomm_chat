import time
from threading import Thread

class RFListener(Thread):
	def __init__(self, dev):
		super(RFListener, self).__init__()
		self._dev = dev
	
	def run(self):
		while True:
			d = None
			try:
				d = open(self._dev)
				print "\033[1;36mDEV\033[0m: Connceted."
			except IOError:
				time.sleep(1)
				continue
			while True:
				message = d.readline()
				if message == "": # Disconnected
					d.close()
					print "\033[1;36mDEV\033[0m: Disconnected."
					break
				message = message.rstrip()
				print "\033[1;34mMSG\033[0m: " + message
		
