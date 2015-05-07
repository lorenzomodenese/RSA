import random
import math
import sys
import Elementary_Function

def encode():
    p=Elementary_Function.GetPrimeNumber(1024)
    print "Generato p casualmente: ",p
    q=Elementary_Function.GetPrimeNumber(1024)
    print "Generato q casualmente: ",q

    #calcolo n e fi di n
    n=q*p
    fi_n=(p-1)*(q-1)
    
    #mi cerco una encryption valida
    while 1:
        e=Elementary_Function.GetPrimeNumber(1024)
        if(e>fi_n/2 and e<fi_n and e%fi_n!=0):
            break


