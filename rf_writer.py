import time
from threading import Thread

class RFWriter(Thread):
	def __init__(self, dev):
		super(RFWriter, self).__init__()
		self._dev = dev
	
	def run(self):
		while True:
			d = None
			print "\033[1;33mSTD\033[0m: Ready for message input."
			message = raw_input().rstrip()
			try:
				d = open(self._dev, "rw")
				d.write(message + "\r\n")
				d.close()
				print "\033[1;36mDEV\033[0m: Message wrote."
			except IOError:
				print "\033[1;36mDEV\033[0m: Not connected."
				continue

