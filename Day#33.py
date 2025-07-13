# Dictionaries in Python

dic = {
    "Harry":"Human Being",
    "Spoon": "Object"
}
# print(dic)
# print(dic["Harry"])

# print(dic["Harry1"])     #this will through error
# print(dic.get("Harry1"))     #this will give you 'None'

# print(dic.keys())
# print(dic.values())

for key in dic:
    print(dic.values())