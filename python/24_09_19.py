def primeNumber(n):
    prime = [ i for i in range(0,n+1) ]

    for i in prime:
        for j in range(2, i):
            if i % j == 0:
                prime[i] = 0
                break
    prime = [i for i in prime[3:] if i != 0 ]
    return prime

primeNumber(50)