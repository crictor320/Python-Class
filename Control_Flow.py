"""
learn about control flow in Python
"""

# IF Statement
# Indentation is 4 spaces
if True:
    print("It is true")

if bool("eggs"):
    print("Yes please!")

if "eggs":
    print("Yes, why not")

h = 50
if h > 50:
    print("Greater than 50")
elif h < 50: #else if
    print("Less than 50")
else:
    print("Equals 50")

print("Done")