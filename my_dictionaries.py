"""
Learn about dictionaries
"""


def main():
    """
    Test function
    :return: 
    """

    urls = {"Google": "www.google.com",
            "Youtube": "www.youtube.com",
            "Facebook": "www.facebook.com",
            "Imgur": "www.imgur.com"}
    print(urls, type(urls))

    #access by key: [key]
    print(urls["Imgur"])

    #build dictionary with dict() constructor
    name_ages = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(name_ages)
    print(d, type(d))

    #another method
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(phonetic)

    #copy a dictionary
    e = phonetic.copy()
    print(e)

    #updating a dictionary: update() method
    stocks = {'GOOG':891, 'AAPL':416, 'IBM':194}
    print(stocks)
    stocks.update({'GOOG':999, 'YHOO':2})
    print(stocks)

    #iteration default is by key value
    for key in stocks:
        print("{k} => {v}".format(k=key, v=stocks[key]))

    #iterate by values
    for val in stocks.values():
        print("val = ", val)

    #iterate by both key and value with: items()
    for items in stocks.items():
        print(items)
    for k, v in stocks.items():
        print(k, v)

    # test for membership via key
    print('GOOG' in stocks)
    print('NVIDIA' not in stocks)

    #deleting: del keyword
    print(stocks)
    del stocks['YHOO']
    print(stocks)

    #mutability of dictionaries
    isotopes = {'H':[1, 2, 3],
                'He':[3,4],
                'Li':[6, 7],
                'Be':[7, 9, 10],
                'B':[10, 11],
                'C':[11, 12, 13, 14]}
    print(isotopes)
    isotopes['H'] += [4, 5, 6, 7]
    print(isotopes)
    isotopes['N'] = [13, 14, 15]
    print(isotopes)


if __name__ == '__main__':
    main()
    exit(0)