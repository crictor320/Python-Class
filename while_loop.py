"""
Learn conditional repetition
Two loops: for-loops and while-loops
"""

counter = 5
while counter != 0:
    print(counter)
    # Augmented Operator
    counter -= 1

counter = 5
while counter:
    print(counter)
    # Augmented Operator
    counter -= 1

# Run Forever: Testing break
while True:
    print("Enter a number")
    response = input() #Take user input
    if int(response) % 7 == 0:   # means number divisible by 7
        break                    # Exit loop



print("Outside while loop")

