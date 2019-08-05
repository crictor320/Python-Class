"""
Learn about lists
unlike strings, lists are mutable.
You can update, and append elements to it
"""
# use [] to define a list
l = [3, 2, 1]
print("List ", l, type(l))

# A list of objects (any type)
a = ["apple", "orange", "pear"]
# Access by index notation
print(a, a[1])
# Replace an element
a[1] = 3.14
print(a, a[1])

# Begin with an empty list, fill a list via prompt until list is full and then print
names = []

total = 0
while total < 3:
    name = input("Enter a name")
    names.append(name) #list if being created and destroyed everytime
    total = total + 1

#display names
print(names)

