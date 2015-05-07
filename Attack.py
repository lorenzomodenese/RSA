import Elementary_Function

def factor(n):
    i = 2
    while True:
        if (n%i == 0):
            return i
        else:
            i = i + 1
            

bits = 28
p = Elementary_Function.getPrimeNumber(bits)
print p
q = Elementary_Function.getPrimeNumber(bits)
print q
print p*q
print factor(p*q)