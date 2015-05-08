import bitarray
import pickle
import socket

import Elementary_Function
import Util

def factor(n):
    if(n%2 == 0):
        return 2
    
    i = 3
    while True:
        if (n%i == 0):
            return i
        else:
            i = i + 2

def receiveKeys(ip, port):
    
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, int(port)))
    
    str = clientSocket.recv(1024)
    list = pickle.loads(str)
    n, e = list

    clientSocket.close()

    return n, e


if __name__ == "__main__":
    
    n, e = receiveKeys(Util.ADDRESS_GATEWAY, Util.PORT_GATEWAY_KEYS)
    print " -> Public Key: ( n , e ) = (", n, ",",e,")"
    #print str(ord(n))
    
    print "Computing . . ."
    p = factor(n)
    q = n//p
    print " ->", n, "= n = p*q =", p, "*", q, "=", p*q
    
    fi = (p-1)*(q-1)
    print " -> fi(n) =", fi
    
    gcd, d, k = Elementary_Function.egcd(e, fi)
    if(d < 0):
        d = d + fi
    print " -> Decryption Key: d =", d
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((Util.ADDRESS_SNIFFER, Util.PORT_SNIFFER))
    s.listen(5)
    
    while True:
        print "Running and waiting . . ."
        clientSocket, address = s.accept()
        
        ip , port = address
        print "Receiving data from", ip
        
        data = ""
        while True:
            str = clientSocket.recv(1024)
            if str == "":
                break
            data = data + str
        
        list = pickle.loads(data)
        
        print "  -> Data received, decrypting . . ."
        
        output = bitarray.bitarray()
        for i in range(0,len(list)):
            m = pow(int(list[i]), int(d), int(n))
            decrypted = bitarray.bitarray("{0:b}".format(m))

            for a in range (len(decrypted), 16):
                decrypted.insert(0,0)
            output.extend(decrypted)

        fout = open(Util.decodedFile, "wb")
        output.tofile(fout)
        fout.close()
        
        print "THE END"
