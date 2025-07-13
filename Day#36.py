# Exception Handling in Python 

'''
try:
    a = int(input("Enter a number: "))
    print(f"\nMultiplication table of {a} is:")
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

print("\n--- Some important lines of code ---")
print("Program ends here")
'''

try:
    num = int(input("enter a number:"))
    a = [1,2,3,4,5,6,7]
    print(a[num])

except ValueError:
    print("enter a valid integer!")
except IndexError:
    print("index error!")
