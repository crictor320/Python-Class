"""
Learn dictionaries
Dictionaries map keys to values.

In some languages are known as associative arrays, hashes or maps.

Create them using {} containing a key-value pair.
Retrieve them by [key value]
"""

d = {'alice': '801-123-8988', 'pedro': '854-542-5478', 'john': '874-852-7777'} # key : value
print(d, type(d))

#access an element
print(d['pedro'])

# Add members to the dictionary, of names-> grades
roster = {} #empty dictionary

total = 0
while total < 3:
    # get the key value
    name = input("Enter a player name")
    # get value associated to key
    score = input("Enter score")
    #add element to dictionary

    roster[name] = score
    total = total + 1

print(roster)