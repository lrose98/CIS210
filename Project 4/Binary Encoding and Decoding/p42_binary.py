'''
CIS 210 Project 4-2: Decimal to Binary to Decimal

Author: Lillie Rose

Credits: Joey Valko
'''

def dtob(n):
    ''' (int) -> str
    Turns a non-negative integer (in base 10) into a binary string (in base2).
    Returns the result.
                #Examples of use:
    >>>dtob(17)
    '10001'
    >>>dtob(128)
    '00000001'
    >>>dtob(1)
    '1'
    '''
    print(bin(n))
    return bin(n)

def btod(b):
    ''' (str) -> int
    Converts a binary string (in base 2) into a non negative-integer (base 10).
    Returns the result.
                #Examples of use:
    >>>btod('100101010')
    298
    >>>btod('0110000')
    48
    >>>btod('11111')
    31
    '''
    digitLength = 0
    length = len(b)
    length = int(length)
    ctdwn = length - 1
    x = 0
    for _ in range(length):
        r = b[x]
        dig = int(r)
        dig = dig * (2**ctdwn)
        digitLength += dig
        ctdwn -= 1
        x += 1
    return digitLength

    

def main():
    ''' (int) -> str, returns None
    Allows input of a non-negative integer (n). Uses dtob(n) to convert n into
    a binary number, prints the result (b). Uses btod(b) to convert n back into
    a non-negative number (n). Prints the result. Returns None.
                #Examples of use:
    >>>main(), 3
    Input a non-negative integer:3
    ...please wait while we convert 3 into binary
    3 in binary(base 2) is: 11
    ...please wait while we convert this binary number back to an integer...
    11 in decimal(base 10) is: 3
    >>>main(), 19
    Input a non-negative integer:19
    ...please wait while we convert 19 into binary
    19 in binary(base 2) is: 11001
    ...please wait while we convert this binary number back to an integer...
    11001 in decimal(base 10) is: 19
    '''
    n = input("Input a non-negative integer:")
    print("...please wait while we convert " + n + " into binary")
    n1 = int(n)
    b = dtob(n1)
    print(n + " in binary(base 2) is: " + b)
    print("...please wait while we convert this binary number back to an integer...")
    n1 = btod(b)

    n = str(n1)
    print(b + " in decimal(base 10) is: " + n)


    return None
