import pickle
import socket

import Elementary_Function
import Util

def factor(n):
    i = 2
    while True:
        if (n%i == 0):
            return i
        else:
            i = i + 1

def receiveKeys(ip, port):
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, int(port)))
    
    str = clientSocket.recv(1024)
    list = pickle.loads(str)
    n, e = list

    clientSocket.close()

    return n, e


if __name__ == "__main__":
    
    n, e = receiveKeys(Util.ADDRESS_SERVER, Util.PORT_GATEWAY)
    print " -> Public Key: ( n , e ) = (", n, ",",e,")"
    #print str(ord(n))
    
    print "Computing . . ."
    p = factor(n)
    q = n//p
    print " ->", n, "= n = p*q =", p, "*", q, "=", p*q
    
    fi = (p-1)*(q-1)
    print " -> fi(n) =", fi
    
    gcd, d, k = egcd(e, fi)
    if(d < 0):
        d = d + fi
    print " -> Decryption Key: d =", d
    
