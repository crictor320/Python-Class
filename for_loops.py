"""
Practice for loops
keyword: for
"""

cities = ["London", "New York", "Madrid", "Paris", "Ogden"]
# iterate over a list
for city in cities:
    print(city)

d = {'alice': '801-123-8988', 'pedro': '854-542-5478', 'john': '874-852-7777'}
# iterate over a dictionary
for item in d:
    print(item, "=>", d[item])  # d[item] gives all elements of the dictionary