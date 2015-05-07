import sys
import socket
import os

def RiceviFile_socket(file_name, porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('', int(porta)))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(1)
    except:
        print "Errore confg iniziale"

    sapp, addr = sock.accept()
    file = open(file_name, 'wb')
    try:
        while 1:
            data = sapp.recv(1024*1)
            if not data:
                break
            file.write(data)

    except Exception as e:
        print e
    finally:
        file.close()
    sock.close()