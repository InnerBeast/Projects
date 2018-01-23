def fibo(num):
    n = 0
    n_one = 1
    print(n)
    print(n_one)
    for i in range(num-2):
        temp = n + n_one
        print(temp)
        n = n_one
        n_one = temp
