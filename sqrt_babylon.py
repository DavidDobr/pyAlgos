"""
calculates and prints sqrt of a number

input: optional: 1 command line argument
prints: sqrt of a number
return: None

"""
from __future__ import print_function
import sys

# Status: DONE

def sqrt_babylon(y, N=1000, prec=0.001):
    """

    :param y: the number to get sqrt of
    :param N: max number of iterations
    :param prec: stop when this precision is reached
    :return: square root of y

    @ToDo: implement solution for square root of negative numbers
    """
    assert (y >= 0), 'Can not sqrt a negative number!'
    if y == 0:
        return 0.0
    else:  # after asserting y>0, this can only have y>0
        n = 0
        x1 = 1.0
        x2 = y
        diff = x1 - x2
        m = (x1 + x2) / 2
        while n < N and abs(diff) > prec:
            m = (x1 + x2) / 2
            if m * m > y:
                x1, x2 = x1, m
            else:
                x1, x2 = m, x2
            diff = x1 - x2
            n += 1
        return m

'''
# test & debugging
test = [0, 1, 2, 3, 4, 10, 20, 100, 200, -10]
for k in test:
    print('sqrt of ', k, ' is ', sqrt_babylon(k), ', err=', \
          round(sqrt_babylon(k) - k ** 0.5, 3))
'''


def GetNumber():
    x = input('> ')
    if x.isdigit():
        x = float(x)
    else:
        print('Enter a number')
        return GetNumber()
    return x


if len(sys.argv) == 1:
    y = GetNumber()
elif len(sys.argv) == 2:
    y = sys.argv[1]  # find square root of Y
    if not y.isdigit():
        print('Enter a number')
        y = GetNumber()
    y = float(y)
else:
    raise Exception('Script only accepts 1 or 2 arguments')

print('sqrt of ', y, ' is ', round(sqrt_babylon(y), 3), ', err=', \
          round(sqrt_babylon(y) - y ** 0.5, 3), sep='')
