'''
CIS 210 Fall 2018
Project 5-1: Binary Recursive

Author: Lillie Rose

Credits: N/A
'''
import math
import doctest

def dtobr(n):
    ''' (int) -> str
    Turns a non-negative integer (in base 10) into a binary string (in base2).
    Returns the result.
                #Examples of use:
    >>> dtobr(17)
    '10001'
    >>> dtobr(128)
    '00000001'
    >>> dtobr(1)
    '1'
    '''
    binary = ""
    if n == 0 or n ==2:
        binary += '0'
        print(binary)
        return binary
    else:
        if n % 2 == 0:
            binary += '0'
        elif n % 2 == 1:
            binary += '1'
        print(binary)
        return binary + dtobr(n // 2)

def btodr(s):
    ''' (str) -> int
    Converts a binary string (in base 2) into a non negative-integer (base 10).
    Returns the result.
                #Examples of use:
    >>> btodr('100101010')
    298
    >>> btodr('0110000')
    48
    >>> btodr('11111')
    31
    '''
    if not s:
        return 0
    else:
        first = s[0]
        x = int(first)
        y= len(s)
        value = x * 2**(len(s) -1)
        return value + btodr(s[1:])

def main():
    '''
    (int) -> str, returns None
    Allows input of a non-negative integer (n). Uses dtob(n) to convert n into
    a binary number, prints the result (b). Uses btod(b) to convert n back into
    a non-negative number (n). Prints the result. Returns None.
                #Examples of use:
    >>> main(n=3)
    Input a non-negative integer: 3
    ...please wait while we convert 3 into binary
    3 in binary(base 2) is: 11
    ...please wait while we convert this binary number back to an integer...
    11 in decimal(base 10) is: 3

    '''
    n = input("Input a non-negative integer:")
    if n == '':
        n=3
    print("...please wait while we convert " + n + " into binary")
    n1 = int(n)
    b = dtobr(n1)
    print(n + " in binary(base 2) is: " + b)
    print("...please wait while we convert this binary number back to an integer...")
    n1 = btodr(b)

    n = str(n1)
    print(b + " in decimal(base 10) is: " + n)
    
print(doctest.testmod())


