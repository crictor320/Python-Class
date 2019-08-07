"""
Learn about collections: tuples, strings, range, list, dictionaries, sets
"""


def do_tuples():
    """
    practice tuples
    :return: nothing
    """
    t = ("Ogden", 1.99, 2)      #use () to define a tuple, immutable sequence of arbitrary objects
    print(t, type(t))
    print("size ", len(t))
    print("one member:", t[0])   #by index notation

    #to iterate over a tuple
    for item in t:
        print(item)

    #single tuples
    t1 = (6,)             #the comma makes this a tuple instead of an int
    print(t1, type(t1))

    #another way to create tuples: parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))


def min_max(items):
    """
    return the min and max elements of a list
    :param items: list collection
    :return: min and max
    """
    return min(items), max(items)



def main():
    """
    test function
    :return: nothing
    """
    #do_tuples()
    print(min_max([56, 76, 11, 12, 90]))


if __name__ == '__main__':
    main()
    exit(0)