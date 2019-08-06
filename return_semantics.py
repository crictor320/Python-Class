"""
Learn about return semantics and function arguments in Python
"""


def egg(var):
    """
    returns the variable back to the user
    :param var: input object
    :return: input onject
    """
    return var


def banner(message, border='*'):
    """
    pass message with a border
    :param message: string message
    :param border: * border
    :return: message with border
    """
    print(border * len(message))
    print(message)
    print(border * len(message))


def sum_two(num1, num2):
    """
    sum of two imput objects
    :param num1: object 1
    :param num2: object 2
    :return: sum of objects
    """
    return num1 + num2


def add_spam(menu=None):   #default for an empty list
    """
    add spam to the menu list
    :param menu:
    :return: menu list
    """
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def main():
    """
    test function
    :return: nothing
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)

    n1 = "peanut"
    n2 = "butter"
    print(n1, " + ", n2, " = ", sum_two(n1, n2))

    #name = input("Enter something")
   #banner(name)
    banner("Weber State", "^")

    breakfast = ['eggs', 'bacon']
    print("Before", breakfast)
    add_spam(breakfast)
    print("After", breakfast)


if __name__ == '__main__':
    main()
    exit(0)