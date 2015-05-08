import os
import pickle
import socket

def InviaLista_socket(lista, ip, porta):

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip, int(porta)))

    clientsocket.send(lista)

    clientsocket.close()


def RiceviData_socket(ipServer, porta):
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ipServer, int(porta)))
    
    str = clientsocket.recv(1024)
    list = pickle.loads(str)
    n, e = list

    clientsocket.close()

    return n, e


