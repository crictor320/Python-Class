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