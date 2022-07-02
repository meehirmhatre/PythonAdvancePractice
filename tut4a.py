'''
iterable

iterator

iteration

generators are iterator which only iterates one time

'''

def gen(n):
    for i in range(n):
        yield i

ob1 = gen(4)
print(ob1)
print(next(ob1))
print(next(ob1))
print(next(ob1))

# num = "345"
# iter1 = iter(num)
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))