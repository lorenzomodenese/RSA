import random
import math
import sys
import Elementary_Function
import Server
import Util

def publishKeys(n,e):
    while 1:
        #nota che la porta deve essere diversa da quella per i dati! da cambiare...
        socket=Server.Server.initServerSocket(Util.ADDRESS_SERVER, Util.PORT_SERVER)
        Server.writeSocket(s, n, e)

def GenerateKey():
    p=Elementary_Function.getPrimeNumber(1024)
    print "  -> Generato p casualmente: ",p
    q=Elementary_Function.getPrimeNumber(1024)
    print "  -> Generato q casualmente: ",q

    #calcolo n e fi di n
    n=q*p
    fi_n=(p-1)*(q-1)
    
    #mi cerco una encryption valida
    while 1:
        e=Elementary_Function.getPrimeNumber(1024)
        if(fi_n%e!=0):
            break

    print "  -> Encryption key: ",e

    #calcolo d
    gcd, d, x =Elementary_Function.egcd(e,fi_n) #la funzione restituisce a*x+b*y=resto, a noi server x
    if(d<0):
        d+=fi_n
    print "  -> Decryption key: ",d

    return n,e,d



if __name__ == "__main__":
    
    n,e,d=GenerateKey()
    try:
        #mi metto in ascolto su un nuovo thread per dare la possibilita a chiunque mi richieda le chiavi di riceverle
        thread.start_new_thread( publishKeys, ("Thread-1", n,e, ) )
    except:
        print "Errore creazione thread"
    ComunicoChiavi(n,e )