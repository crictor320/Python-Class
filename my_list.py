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
    print()


if __name__ == '__main__':
    main()
    exit(0)