#sorted list only

import bisect

a = [11, 4, 5, 15, 45, 54, 85, 564]
print(bisect.bisect(a,7))
bisect.insort(a, 7)
print(a)