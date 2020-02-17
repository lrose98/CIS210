'''
CIS 210 Fall 2018
Project 2-1: Determining Net Pay

Author: Lillie Rose

Credits: N/A
'''

def tax(grosspay):
    ''' (number) -> number
    Return the tax of the gross pay, give that the tax
    rate is 15%
            #Examples of use:
    >>> tax(10)
    1.5
    >>> tax(40)
    6.0
    >>> tax(15)
    2.25
    '''
    minus = grosspay * .15

    return minus

def netpay(hours):
    '''
    Times hours work by the hourly rate(10.75) to get the
    grosspay. Call tax(grosspay) in order to get the tax.
    Minus the grosspay by the tax. Return the result.
            #Examples of use:
    >>> tax(10)
    91.375
    >>> tax(40)
    365.5
    >>> tax(15)
    137.0625
    '''
    grosspay = hours * 10.75
    tax(grosspay)

    pay = grosspay - tax(grosspay)

    return pay

def main():
    '''
    '''
    print ('For 10 hours work, netpay is: ', netpay(10))
    print ('For 40 hours work, netpay is: ', netpay(40))
    return None

main()
