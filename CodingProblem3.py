#find all prime numbers
#save to file

def isPrime(n):
    if(n == 1):
        return True
    for i in range(2, int(n/2)+2):
        if(n%i == 0):
            return False
    return True


i = 1
while True:
    if(isPrime(i)):
        print(i)
    i+=1
