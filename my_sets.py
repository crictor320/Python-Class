"""
Learn about sets
An unordered collection of unique, immutable objects
Define it using { }
You can use the set() constructor to create one
"""


def main():
    """
    Test function
    :return: 
    """
    p = {8, 9, 7, 15, 92}
    print(p, type(p))
    data = [1, 3, 87, 156, 1, 3]
    print(data, type(data))

    #eliminate duplicates
    sdata = set(data)       #the 1, 3 are combined
    print(sdata, type(sdata))

    #iterate with for loop
    for item in sdata:
        print(item)

    #supports membership testing: in, not it
    print(156 in sdata)

    #adding elements to sets:
    sdata.add(45)
    print(sdata)
    sdata.update([2, 5, 5, 5, 5, 8, 7, 9, 2, 3, 6,])
    print(sdata)

    #removing elemets
    #remove() raises keyerror if not found
    sdata.remove(87)
    print(sdata)
    #sdata.remove(77)
    #print(sdata)

    #discard() does not raise any error
    sdata.discard(77)
    print(sdata)

    #copying sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)

    ###############################Define some sets
    blue_eyes = {"Olivia", "Harry", "Lily", "Jack"}
    blond_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry", "Lily", "Amelia", "Lola"}
    o_blood = {"Mia", "Joshua", "Lily", "Olivia"}
    b_blood = {"Amelia", "Jack"}
    a_blood = {"Harry"}
    ab_blood = {"Joshua", "Lola"}

    print(blue_eyes.union(blond_hair))      #union(): as long as its one of the two
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))


if __name__ == '__main__':
    main()
    exit(0)