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
        sapp.close()

def GenerateKey():
    dim=raw_input("Inserire numero di bit per le chiavi: ")
    p=Elementary_Function.getPrimeNumber(int(dim))
    print "\n  -> Generato p casualmente: ",p
    q=Elementary_Function.getPrimeNumber(int(dim))
    print "\n  -> Generato q casualmente: ",q

    #calcolo n e fi di n
    n=q*p
    fi_n=(p-1)*(q-1)
    
    #mi cerco una encryption valida
    while 1:
        e=Elementary_Function.getPrimeNumber(int(dim))
        if(fi_n%e!=0 and e<fi_n):
            break

    print "\n  -> Encryption key: ",e

    #calcolo d
    gcd, d, x =Elementary_Function.egcd(e,fi_n) #la funzione restituisce a*x+b*y=resto, a noi server x
    if(d<0):
        d+=fi_n
    print "\n  -> Decryption key: ",d
    print "\n  -> N key: ",n
    print "  -> (e, fi(n))=", gcd
    return n,e,d



if __name__ == "__main__":
    print "Inizio RSA"
    n,e,d=GenerateKey()
    try:
        #mi metto in ascolto su un nuovo thread per dare la possibilita a chiunque mi richieda le chiavi di riceverle
        thread.start_new_thread( publishKeys, ("Thread-1", n,e, ) )
    except Exception as w:
        print w,"Errore creazione thread"

    socket=Server.Server.initServerSocket(Util.ADDRESS_SERVER, Util.PORT_SERVER)
    while 1:
        print "\nPronto a ricevere file cifrati..."
        sapp, ip=socket.accept()
        stringa_cifrata=Server.Server.readSocket(sapp)
        cypher_list_deserialized=pickle.loads(stringa_cifrata)
        sapp.close()
        
        ############################## parte inutile
        #scrivo il file cifrato (anche se non mi serve a niente, ma solo per farlo vedere a mazzini
        output_cifrato=bitarray()
        for i in range(0,len(cypher_list_deserialized)):
            cifrato_bitarray=bitarray("{0:b}".format(cypher_list_deserialized[i]))
            output_cifrato.extend(cifrato_bitarray)
        
        fOutCifrato=open(Util.encodedFile, "wb")
        output_cifrato.tofile(fOutCifrato)
        fOutCifrato.close()
        ##############################
        
        print "  -> Ricevuto un file, ora posso decifrare!"
        
        output = bitarray()
        for i in range(0,len(cypher_list_deserialized)):
            decifrato= pow(int(cypher_list_deserialized[i]), int(d), int(n))
            decifrato_bitarray=bitarray("{0:b}".format(decifrato))

            for a in range (len(decifrato_bitarray), 16): #16 corrisponde alla dimensione dei chunk da elaborare
                decifrato_bitarray.insert(0,0)
            output.extend(decifrato_bitarray)


        fOut=open(Util.decodedFile, "wb")
        output.tofile(fOut)
        fOut.close()
        print "Fine decifratura"
    
        time.sleep(1)

