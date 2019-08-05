"""
Learn about functions/definitions
Use the keyword: def <name>():
"""


def even_or_odd(number):
    """
    Find if number is even of odd
    :param number: input number
     print "even" on even numbers
             "odd" on odd numbers
    """
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

# call function
even_or_odd(89)
even_or_odd(22)