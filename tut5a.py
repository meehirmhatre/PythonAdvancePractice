'''

  List comprehensions
  Dictionary comprehensions
  Set comprehensions
  Generator comprehensions

'''

list_1 = [1, 34, 35, 22, 456, 3213, 3423, 12, 2]

divide_by_3 = []

for i in list_1:
    if i % 3 == 0:
        divide_by_3.append(i)

print(divide_by_3)

print("list compreension", [item for item in list_1 if item % 3 == 0])

dict1 = {'a': 22, 'b': 56, 'A': 5}
print("dict comp", {k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

set1 = {x ** 2 for x in [1, 2, 3, 4, 4, 4, 5, 5,  5 ]}
print(set1)


gen = (i for i in range(56) if i%3==0)

for item in gen:
    print(item)

print(gen)