"""
Strings and Collections

A String is a immutable sequence of Unicode code-points
"""

print('This is a string')
print("This is a string too")

# Concatenation and Adjacent Strings
s1 = "First"
s2 = "Second"
print(s1 + s2)

# Multiline Strings and Newlines
s3 = """This is 
a multi-line
string"""
print(s3)

s4 = "This is\na multi-line\nstring"
print(s4)

# Support for backslash
s5 = "A \\ in a string"
print(s5)

s6 = 'this is "wow"'
print(s6)

# Raw Strings - ignores all the formatting stuff
raw_string = r'C:\stuff\stuff\stuff'
print(raw_string)

# Strings as sequence
p = "parrot"
print("s[4]", p[4], type(p))  #index notation - prints 4th index, and object type which is a string
print(p, p.capitalize())    #s.capitalize() capitalizes the first first letter