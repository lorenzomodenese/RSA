import socket
import os

import Util

def keysExchange():
    
    inSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    inSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    inSocket.bind((Util.ADDRESS_GATEWAY, Util.PORT_GATEWAY_KEYS))
    inSocket.listen(5)
    
    print "Running and waiting KeysTCP . . ."
    
    while True:
        
        clientSocket, address = inSocket.accept()
        
        pid = os.fork()
        
        if(pid == 0):
            try:
                inSocket.close()
                
                #data = ""
                #while True:
                #    string = clientSocket.recv(1024)
                #    data = data + string
                #    if len(string) < 1024:
                #        break
                
                ip, port = address
                print "\tConnetion received from", ip, ":", port
                
                outSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                outSocket.connect((Util.ADDRESS_SERVER, Util.PORT_SERVER_KEYS))
                
                #outSocket.send(data)
                
                data = ""
                while True:
                    string = outSocket.recv(1024)
                    if not string:
                        break
                    data = data + string
                
                print "\tData received from server"
                    
                outSocket.close()
                
                clientSocket.send(data)
                
            except Exception as e:
                print e
                print("Error!")
                
            finally:
                clientSocket.close()
                os._exit(0)
        else:
            clientSocket.close()
