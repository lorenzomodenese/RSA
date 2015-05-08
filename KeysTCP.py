import socket
import os

global inIP
inIP = "172.1.1.1"

global inPORT
inPORT = 9091

global outIP
outIP = "172.1.2.2"

global outPORT
outPORT = 2021

def keysExchange():
    
    inSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    inSocket.bind((inIP, inPORT))
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
                outSocket.connect((outIP, outPORT))
                
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
