"""
Get a file from the web: http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

task 1: Count number of words in document
"""

from urllib.request import urlopen
file = r"http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

counter = 0
data = {}
with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()   #decodes the btyes and adds a space between each entity
        #print(words)
        for word in words:
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
            counter += 1
print("Total number of words", counter)
  #sort by keys

            for key in sorted(data.keys()):
               print(key, data[key])



