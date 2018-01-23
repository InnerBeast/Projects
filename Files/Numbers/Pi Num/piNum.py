import math
num = input("Type how many digits of pi you want to see after the decimal point: ")
num = int(num)
num = round(math.pi,num)
print(num)
