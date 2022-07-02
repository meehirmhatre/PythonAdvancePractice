'''
Map function
map(fuction_to_apply, list of inputs)
'''

h1 = [1,2,3,5,7]

def sq1(x):
    return x**2

sq = list(map(sq1, h1))

print(sq)