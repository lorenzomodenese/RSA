import socket
import os

def InviaFile_socket(nome_file, ip, porta):

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, int(porta)))

    file = open(nome_file, "r")

    while 1:
        stringa = file.read(1024)
        clientsocket.send(stringa)
        if stringa == "":
            break
    file.close()

    clientsocket.close()


def RiceviData_socket(ipServer, porta):
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ipServer, int(porta)))
    
    n=clientsocket.recv(1024)
    clientsocket.send('y')
    e=clientsocket.recv(1024)

    clientsocket.close()

    return n,e

