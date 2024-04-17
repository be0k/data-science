import numpy as np

def isPrime(n):
    tmp = 1
    for i in range(2,int(np.floor(np.sqrt(n)))+1):
        if(not n%i):
            tmp = 0
            break
    return n, tmp

#2~32767
num = np.random.randint(2,32768)
print(*isPrime(7))