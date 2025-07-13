# String Methods in Python

'''
a = "!@#Harry!@#"   #strings are immutables
print(a.upper())
print(a.lower())
print(a.rstrip("!@#"))
print(a.replace("H","M"))

b = "Abhay is a good boy"
print(b.split(" "))

blockheading = "introduction to js"
print(blockheading.capitalize())

str1 = "welcome to the console!!"
# print(len(str1))
print(str1.center(50))
print(str1.count("o"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to",4,10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "        "  # using Spacebar
print(str1.isspace())
str2 = "        "  # using Tab
print(str2.isspace())

str2 = "To kill a Mocking bird"
print(str2.istitle())
'''

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())