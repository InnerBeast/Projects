from function import findprimefactor
num = input("Enter a number you want to see the prime factors of: ")
num = int(num)
listofPrimes = findprimefactor(num)
print(listofPrimes)
