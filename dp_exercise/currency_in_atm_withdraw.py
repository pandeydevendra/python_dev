'''
indian currency ; 100,200,500,2000
ask amount,
validity of amount (in mutliple of 100......)denomination
withdraw amount i minimum currency
count number of currency separately

steps:
1.amount:
2.amount = 2000*b + r
3.amount//2000 =a1
4.amount%2000 = r1
3.r1%500 = r2
4.r2%200 = r3
5.r3/100 =
'''


def currency_count(amount):
    """
    :param amt:
    :return: dict  {2000: n1, 500: n2, 200: n3, 100:, n4}
    """
    currency_lists = [2000, 500, 200, 100]
    count = amount // 2000
    print("Number of 2000 currency is {}.".format(count))
    amount = amount % 2000
    count = amount // 500
    print("Number of 500 currency is {}.".format(count))
    amount = amount % 500
    count = amount // 200
    print("Number of 200 currency is {}.".format(count))
    amount = amount % 200
    count = amount // 100
    print("Number of 100 currency is {}.".format(count))


def currency_count_loop(amount):
    """
    :param amt:
    :return: dict  {2000: n1, 500: n2, 200: n3, 100:, n4}
    """

    currencies = [2000, 500, 200, 100]
    for currency in currencies:
        # print(currency)
        count = amount // currency

        # TODO: will implement currecncy count dictionary here.

        print("Number of {} currency is {}.".format(currency, count))
        amount = amount % currency


amount = int(input("Enter amount: "))

if amount % 100 == 0:
    print("Entered amount {} is valid.".format(amount))
    currency_count_loop(amount)
else:
    print("Entered amount {} is not valid.".format(amount))
