"""
Simulate 6000 rolls of a die (1-6)
"""
import random
import statistics

def roll_die(num):
    """
    random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 maps to 1
    Index 1 maps to 2...ect
    """
    freq = [0] * 6      #list initial values to 0
    for roll in range(num):
        n = random.randint(1, 6)
        freq[n - 1] += 1
        #print(random.randint(1, 6))
    return freq



def main():
    """
    Test function
    :return: 
    """
    num = int(input("How many times you need to roll: "))
    results = roll_die(num)
    for roll, total in enumerate(results):
        print("Total rolls of {} = {}".format(roll, total))

    print("Average = {}".format(sum(results)/len(results)))
    print("Mean = {}".format(statistics.mean(results)))
    print("Median = {}".format(statistics.median(results)))



if __name__ == '__main__':
    main()
    exit(0)