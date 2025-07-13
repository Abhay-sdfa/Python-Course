# Operations in Tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)        # Convert tuple to list
# temp.append("Russia")         # Add item
temp.pop(3)                   # Remove item at index 3 ("England")
# temp[2] = "Finland"           # Change item at index 2 ("India" → "Finland")
countries = tuple(temp)       # Convert list back to tuple
# print(countries)              # Print final tuple
 
res = countries.count("Spain")
print("the count of spain is",res)