# If Else Conditional Statements in Python

# a = int(input("enter your age: "))
# print("you entered age is ",a)
# if (a>18):
#     print("you can drive")
# else:
#     print("you can't drive")

# conditionals operators
# <,>,<=,>=,!=.==

# print(a==18)
# print(a>18)
# print(a<18)
# print(a<=18)
# print(a>=18)

# applePrice = 210
# budget = 200
# if (applePrice <= budget):
#     print("Alexa, add 1kg Apples to the cart.")
# else:
#     print("Alexa, do not add Apples to the cart.")

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")