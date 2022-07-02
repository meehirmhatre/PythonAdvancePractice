from functools import reduce

def sum_1(a,b):
    return a+b
lil = reduce(sum_1, [1,2,3,4])

print(lil)