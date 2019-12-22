def fact(n):

    res = 1

    for i in range(n):
        res *= i+1

    return (res)

def n_C_k(n,k):

    return int(fact(n)/(fact(k)*fact(n-k)))


total = 0
for i in range(400,601):
    total += n_C_k(1000,i)

print (total/2**1000)
