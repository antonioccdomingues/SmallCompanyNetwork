import socket
import signal
import sys
import psutil
import time
import struct

def signal_handler(sig, frame):
	print('\nDone!')
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

ip_addr = "127.0.0.1"
udp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	
	
	time.sleep(4)
	message=(psutil.cpu_percent())
	a=dict(psutil.virtual_memory()._asdict())
	b=a.get("percent")
	cpu=("\nPercentagem de utilizaçao do cpu: "+str(message)+"%").encode()
	free=("\nPercentagem de memoria utilizada: " +str(b)+"%").encode()
	sock.sendto(cpu+free, (ip_addr, udp_port))
	

