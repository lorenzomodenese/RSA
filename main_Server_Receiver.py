import random
import math
import sys
import Elementary_Function
import Server
import Util
from bitarray import bitarray
import time
import thread
import pickle

def publishKeys(nome,n,e):
    print "Pronto a fornire le chiavi..."
    #nota che la porta deve essere diversa da quella per i dati porta 9091!
    socket=Server.Server.initServerSocket(Util.ADDRESS_SERVER, Util.PORT_SERVER_KEYS)
    while 1:
        sapp, ip=socket.accept()
        Server.Server.writeSocket(sapp, n, e)
        print "  -> Fornite keys a ",ip

def GenerateKey():
    p=Elementary_Function.getPrimeNumber(1024)
    print "\n  -> Generato p casualmente: ",p
    q=Elementary_Function.getPrimeNumber(1024)
    print "\n  -> Generato q casualmente: ",q

    #calcolo n e fi di n
    n=q*p
    fi_n=(p-1)*(q-1)
    
    #mi cerco una encryption valida
    while 1:
        e=Elementary_Function.getPrimeNumber(1024)
        if(fi_n%e!=0):
            break

    print "\n  -> Encryption key: ",e

    #calcolo d
    gcd, d, x =Elementary_Function.egcd(e,fi_n) #la funzione restituisce a*x+b*y=resto, a noi server x
    if(d<0):
        d+=fi_n
    print "\n  -> Decryption key: ",d
    print "\n  -> N key: ",n

    return n,e,d



if __name__ == "__main__":
    print "Inizio RSA"
    n,e,d=GenerateKey()
    try:
        #mi metto in ascolto su un nuovo thread per dare la possibilita a chiunque mi richieda le chiavi di riceverle
        thread.start_new_thread( publishKeys, ("Thread-1", n,e, ) )
    except Exception as w:
        print w,"Errore creazione thread"

    print "\nPronto a ricevere file cifrati..."
    output = bitarray()
    socket=Server.Server.initServerSocket(Util.ADDRESS_SERVER, Util.PORT_SERVER)
    while 1:
        sapp, ip=socket.accept()
        stringa_cifrata=Server.Server.readSocket(sapp)
        cypher_list_deserialized=pickle.loads(stringa_cifrata)
        
        print "  -> Ricevuto un file, ora posso decifrare!"

        for i in range(0,len(cypher_list_deserialized)):
            decifrato= pow(int(cypher_list_deserialized[i]), int(d), int(n))
            decifrato_bitarray=bitarray("{0:b}".format(decifrato))
            for a in range (len(decifrato_bitarray), 64):
                decifrato_bitarray.insert(0,0)
            output.append(decifrato_bitarray)


        while output[output.length()-1]==0:
            output.pop(output.length()-1)
        output.fill()

        fOut=open(Util.decodedFile, "wb")
        output.tofile(fOut)
        fOut.close()
        print "Fine decifratura"
    
        time.sleep(1)

