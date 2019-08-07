"""
Learn about range() collection
"""


def main():
    """
    Test function
    :return: 
    """
    s = "show how to do it".split()
    print(s, type(s))
    #access by index
    print("s[3]:", s[3])
    print("last member:", s[len(s) - 1])    #very un-pythonic
    #better way
    print("s[-1]:", s[-1])

    #slicing
    print(s)
    print("From 1st to one before the last member:", s[1:-1])
    print("From 1st to third member:", s[1:3])
    print("From 1st to the end:", s[1:])
    print("From beginning to a position:", s[:2])
    print("access to everything:", s[:])

    #make a copy of the list
    t = s                   #shallow copy
    print("t: ", t)
    print("s: ", s)
    print("t is s:", t is s)

    t = s[:]                 #deep copy; t = s.copy() or t = list(s)
    print("t: ", t)
    print("s: ", s)
    print("t is s:", t is s)
    print("t == s:", t == s)

    #shallow copies
    #a list of lists
    a = [[1, 2], [3, 4]]
    print(a, type(a))
    print("a[0]:", a[0])
    print("a[0][1]:", a[0][1])  #access exact member

    #copy the list of lists
    b = a[:]
    print(b)
    a[0][1] = 25
    print(a)

    #repetition
    c = [21, 37]
    d = c * 4
    print(c)
    print(d)
    s = [[5, 7]] * 5
    print(s)
    s[1].append(7)
    print(s)
    s[2].append(7)
    print(s)


    #index()
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')      #searches for a value
    print("The index of 'fox' entry is: ", i, w[i])

    #a value error is called if an index is not found
    #i = w.index('cat')
    #print("The index of 'cat' entry is: ", i, w[i])

    #membership testing with: count()
    print("'the' value is: ", w.count("the"))

    #also test membership with: in, not in
    print(37 in [12, 22, 37, 99])
    print(78 not in [12, 22, 37, 99])

    #removing elements from list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    del w[3]        #deletes fox
    print(len(w), w)

    #remove using: remove()
    w.remove("over")
    print(len(w), w)
    del w[w.index('dog')]
    print(len(w), w)

    #rearranging lists of elements
    g = [1, 11, 21, 1211, 112111]
    print("g:", g)
    g.reverse()         #this is a permanent change
    print("reverse g:", g)
    g.reverse()
    print("reverse g again:", g)

    #sort method accepts two arguments, key and reverse
    d = [8, 9, 1, 54, 100, 7]
    print("      d:", d)
    d.sort()
    print("   sort:", d)
    d = [8, 9, 1, 54, 100, 7]
    d.sort(reverse=True)
    print("reverse:", d)

    #sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print("w:    ", w)
    w.sort(key=len)     #sort by length
    print("sort: ", w)




if __name__ == '__main__':
    main()
    exit(0)