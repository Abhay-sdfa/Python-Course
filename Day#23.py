# List methods in python

l = [11,45,24,3,4,5,86]
l.append(6)
# print(l)
l.sort(reverse=True)
# print(l)
# print(l.count(11))
m = l.copy()
m[0] = 0
# print(m)
l.insert(1,899)
print(l)