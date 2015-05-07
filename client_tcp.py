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

