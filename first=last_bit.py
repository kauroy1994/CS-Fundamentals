from math import floor
def bit(n,pad = 4):

    if n == 0:
        return [int(x) for x in list(pad*'0')]
    
    res = []
    
    q = n
    
    while (q != 1):
        #print (res)
        #print (q)
        #input()
        res = [q % 2] + res
        q = floor(q / 2)

    res = [1] + res

    padding_len = pad - len(res)

    res = [int(x) for x in padding_len*'0'] + res

    return (res)

c = 0

for i in range(16):

    bits = bit(i)

    if bits[0] == bits[3]:
        c += 1

print (c)

#=================even-heads=================
c1 = 0
for i in range(16):
    bits = bit(i)

    if sum(bits)%2 == 0:
        c1 += 1

print (c1)
        

    

        
