import socket
import os

import Util

def dataMirroring():
	
	inSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	inSocket.bind((Util.ADDRESS_GATEWAY, Util.PORT_GATEWAY))
	inSocket.listen(5)
	
	print "Running and waiting DataMirroringTCP . . ."
	
	while True:
		
		clientSocket, address = inSocket.accept()
		
		pid = os.fork()
		
		if(pid == 0):
			try:
				inSocket.close()
				
				data = ""
				while True:
					string = clientSocket.recv(1024)
					if not string:
						break
					data = data + string
				
				ip, port = address
				print "\tData received from", ip
				
				outSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				outSocket.connect((Util.ADDRESS_SERVER, Util.PORT_SERVER))
	
				mirrorSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				mirrorSocket.connect((Util.ADDRESS_SNIFFER, Util.PORT_SNIFFER))
				
				outSocket.send(data)
				mirrorSocket.send(data)
				
				outSocket.close()
				mirrorSocket.close()
				
			except Exception as e:
				print e
				print("Error!")
				
			finally:
				clientSocket.close()
				os._exit(0)
		else:
			clientSocket.close()

