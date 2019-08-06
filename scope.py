"""
Learn about scoping in Python
L - local
E - enclosing
G - global
B - built-in
"""
count = 0   #global object


def set_count(n):
    """
    display set count
    :param n: input count
    :return: nothing
    """
    global count     #ties this to the global variable
    count = n


def show_count():
    """
    display the current count
    :return: nothing
    """
    print(count)


def main():
    """
    test function
    :return: nothing
    """
    show_count()
    set_count(9)
    show_count()

if __name__ == '__main__':
    main()
    exit(0)