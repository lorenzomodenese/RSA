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


if __name__ == "__main__":
    n,e=RiceviKeys()
    print "  -> Encryption Key: ",e
    print "  -> N: ",n


