import random
import math
import sys
import Elementary_Function
import Client
import Util
from bitarray import bitarray
import pickle
import time


def RiceviKeys(ip_server):
    n,e=Client.RiceviData_socket(ip_server, Util.PORT_SERVER_KEYS)
    return n,e

def encode_and_send(e, n,ip_server):
    bytes = bitarray()
    data = bitarray()
    output = bitarray()

    with open (Util.inputFile, "rb") as f:
        bytes.fromfile(f)
    print "Data length del file:", ((bytes.length()/8)/1024), "KB\n"

    #16 corrisponde alla dimensione dei chunk da elaborare
    for i in range(bytes.length()%16):
        bytes.extend("0")

    cypher_list=[]
    print "Inizio cifratura"
    start = time.time()
    for i in range(bytes.length()/16):
        data = bytes[(0+(16*i)):(16+(16*i))]
        message=int(data.to01(),2)
        cypher= pow(int(message), int(e), int(n))
        cypher_list.append(cypher)

    print "Encoded succesfully: elapsed time", time.time()-start, "seconds."
    print "Serializzo il cifrato"
    cypher_list_serialized=pickle.dumps(cypher_list)
#print "primo numero lista : ", cypher_list[0]
#print "primo numero lista : ", cypher_list[len(cypher_list)-1]

    #invio cypher_list
    print "Invio il cifrato"
    Client.InviaLista_socket(cypher_list_serialized, ip_server, Util.PORT_GATEWAY)


if __name__ == "__main__":
    ip_server= raw_input("Inserisci IP Server: ")
    n,e=RiceviKeys(ip_server)
    print "  -> Encryption Key: ",e
    print "  -> N: ",n
    encode_and_send(e,n,ip_server)



