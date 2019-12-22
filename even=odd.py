n = 6
x = [[int(i) for i in list(str(j))] for j in range(10**n)]
x = [[int(k) for k in list((n-len(i))*'0') + i] if len(i) < n else i for i in x]
c = 0
for number in x:
    ec,oc = 0,0
    for digit in number:
        if digit % 2 == 0:
            ec += 1
        else:
            oc += 1
    if ec == oc:
        c += 1

print (c) #for 6 it is 6C3*(5^4) = 312500
        
