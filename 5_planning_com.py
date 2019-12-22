#number of ways to form 5 member committee with only one from one couple
from itertools import permutations,combinations
combs = list(combinations('0123456789',5))
combs = [list(x) for x in combs]
combs = [[int(i) for i in x] for x in combs]
c = 0
for comb in combs:
    bool_comb_sum = sum([1 for i in comb if ((i%2 == 0) and (i+1 in comb))])
    if bool_comb_sum == 0:
        c += 1
print (c)

