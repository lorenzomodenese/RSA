import socket
import os

def InviaLista_socket(lista, ip, porta):

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, int(porta)))

    clientsocket.send(lista)

    clientsocket.close()


def RiceviData_socket(ipServer, porta):
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ipServer, int(porta)))
    
    n=clientsocket.recv(1024)
    clientsocket.send('y')
    e=clientsocket.recv(1024)

    clientsocket.close()

    return n,e


