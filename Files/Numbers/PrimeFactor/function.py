def checkPrime(number):
    for num in range(2,int(number/2)+1):
        if (number % num == 0):
            return False
    return True

def findprimefactor(num):
    primes = []
    for i in range(2,int(num / 2) + 1):
        if(num % i == 0):
            if(checkPrime(i)):
                primes.append(i)
    return primes
