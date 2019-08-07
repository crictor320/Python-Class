"""
Learn about exceptions
"""
import sys

def convert(s):
    """
    converts a string to integer
    :param s:
    :return:
    """

    try:
        return int(s)
    except (ValueError, TypeError) as error:
        print("Conversion error {}"\
              .format(str(error)), file=sys.stderr)
    return -1


def sqrt(x):
    """
    Compute the sqrt using the method of Heron of Alexandria
    :param x: number to compute the sqrt
    :return: the sqrt of x
    :raise: ValueError() on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


def main():
    """
    Test function
    :return: 
    """
    #print(convert("11"))
    #print(convert("Hello"))
    #print(convert([1, 4, 8]))
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannont compute the value of negative numbers")

    print("Done")


if __name__ == '__main__':
    main()
    exit(0)