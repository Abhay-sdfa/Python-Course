# Introduction to lists in python 

lst1 = [1, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
# print(lst1)
# print(lst2)

# if "Green" in lst2:
#     print("Yes")
# else:
#     print("No")

# print(lst1[:])
# print(lst1[1:6:3])

# list comprehension
list = [i for i in range(4)]
# print(list)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

numwith_even = [num for num in lst1 if num%2 == 0]
print(numwith_even)