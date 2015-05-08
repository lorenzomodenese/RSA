import random
import math
import sys
import Elementary_Function
import Client
import Util
from bitarray import bitarray


def RiceviKeys():
    ip_server= raw_input("Inserisci IP Server: ")
    n,e=Client.RiceviData_socket(ip_server, Util.PORT_SERVER_KEYS)

    return n,e

def encode():
    bytes = bitarray()
    data = bitarray()
    output = bitarray()

    with open (Util.inputFile, "rb") as f:
        bytes.fromfile(f)
    print "Data length:", ((bytes.length()/8)/1024), "KB\n"

    for i in range(bytes.length()%64):
        bytes.extend("0")

    for i in range(bytes.length()/64):
        data = bytes[(0+(64*i)):(64+(64*i))]



if __name__ == "__main__":
    n,e=RiceviKeys()
    print "  -> Encryption Key: ",e
    print "  -> N: ",n
    print str(ord(n))


