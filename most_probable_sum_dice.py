from random import randint

x = [0 for i in range(12)]

for i in range(6):
    for j in range(6):
        x[((i+1)+(j+1))-1] += 1

print ([round(i/sum(x),2) for i in x])

emp_x = [0 for i in range(12)]

for i in range(10000):

    d1 = randint(1,6)
    d2 = randint(1,6)

    emp_x[d1+d2-1] += 1

print ([j/sum(emp_x) for j in emp_x])

    


