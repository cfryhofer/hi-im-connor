def exactChange(userTotal):
    if (userTotal <= 0):
        return None
    else:
        numdollars = userTotal // 100
        userTotal %= 100

        numquarters = userTotal // 25
        userTotal %= 25

        numdimes = userTotal // 10
        userTotal %= 10

        numnickels = userTotal // 5
        numpennies = userTotal % 5

        return (numdollars, numquarters, numdimes, numnickels, numpennies)


def main():
    n = int(input())
    res = exactChange(n)
    if(res == None):
        print("no change")
    else:
        numdollars = res[0]
        numquarters = res[1]
        numdimes = res[2]
        numnickels = res[3]
        numpennies = res[4]

        if numdollars > 0:
            if numdollars == 1:
                print('%d dollar' % numdollars)
            else:
                print('%d dollars' % numdollars)

        if numquarters > 0:
            if numquarters == 1:
                print('%d quarter' % numquarters)
            else:
                print('%d quarters' % numquarters)

        if numdimes > 0:
            if numdimes == 1:
                print('%d dime' % numdimes)
            else:
                print('%d dimes' % numdimes)

        if numnickels > 0:
            if numnickels == 1:
                print('%d nickel' % numnickels)
            else:
                print('%d nickels' % numnickels)

        if numpennies > 0:
            if numpennies == 1:
                print('%d penny' % numpennies)
            else:
                print('%d pennies' % numpennies)

main()
