'''
Project 6-1: Automated Testing
Write a function to test the string reverse functions from Project 5-2.
Author:Lillie Rose

Credits: Stack Overflow threads
'''

import p52_stringreverse as p5

def test_reverse(f):
    '''
    Test the funcitons stringReverseR(S) and stringReverseI(S).
                #Examples of use:
    >>> test_reverse(p5.strReverseR)
    Checking <function strReverseI at 0x043D8780>('')... its value '' is correct!
    Checking <function strReverseI at 0x043D8780>('a')... its value 'a' is correct!
    Checking <function strReverseI at 0x043D8780>('aaaa')... its value 'aaaa' is correct!
    Checking <function strReverseI at 0x043D8780>('abc')... its value 'cba' is correct!
    Checking <function strReverseI at 0x043D8780>('hello')... its value 'olleh' is correct!
    Checking <function strReverseI at 0x043D8780>('racecar')... its value 'racecar' is correct!
    Checking <function strReverseI at 0x043D8780>('testing123')... Error has wrong value '321gnitset', expected '321gnitest'!
    Checking <function strReverseI at 0x043D8780>('a')... Error has wrong value 'a', expected 'b'!
    Checking <function strReverseI at 0x043D8780>('CIS 210')... Error has wrong value '012 SIC', expected '012 SIC#'!
    >>> test_reverse(p5.strReverseI)
    Checking <function strReverseI at 0x043187C8>('')... its value '' is correct!
    Checking <function strReverseI at 0x043187C8>('a')... its value 'a' is correct!
    Checking <function strReverseI at 0x043187C8>('aaaa')... its value 'aaaa' is correct!
    Checking <function strReverseI at 0x043187C8>('abc')... its value 'cba' is correct!
    Checking <function strReverseI at 0x043187C8>('hello')... its value 'olleh' is correct!
    Checking <function strReverseI at 0x043187C8>('racecar')... its value 'racecar' is correct!
    Checking <function strReverseI at 0x043187C8>('testing123')... Error has wrong value '321gnitset', expected '321gnitest'!
    Checking <function strReverseI at 0x043187C8>('a')... Error has wrong value 'a', expected 'b'!
    Checking <function strReverseI at 0x043187C8>('CIS 210')... Error has wrong value '012 SIC', expected '012 SIC#'!
    '''
    testlist= ['', 'a', 'aaaa', 'abc', 'hello', 'racecar', 'testing123', 'a', 'CIS 210']
    listtest= ['', 'a', 'aaaa', 'cba', 'olleh', 'racecar', '321gnitest', 'b', '012 SIC#']
    i= 0
    while i < 9:
        S= testlist[i]
        output= f(S)
        if listtest[i] == output:
            print('Checking {}(\'{}\')... its value \'{}\' is correct!'.format(f, testlist[i], output))
        else:
            print('Checking {}(\'{}\')... Error has wrong value \'{}\', expected \'{}\'!'.format(f, testlist[i], output, listtest[i]))
        i+= 1
    return None

def main():
    '''calls string reverse test func 2 times
                #Examples of use:
    >>> main()
    Checking <function strReverseR at 0x043186F0>('')... its value '' is correct!
    Checking <function strReverseR at 0x043186F0>('a')... its value 'a' is correct!
    Checking <function strReverseR at 0x043186F0>('aaaa')... its value 'aaaa' is correct!
    Checking <function strReverseR at 0x043186F0>('abc')... its value 'cba' is correct!
    Checking <function strReverseR at 0x043186F0>('hello')... its value 'olleh' is correct!
    Checking <function strReverseR at 0x043186F0>('racecar')... its value 'racecar' is correct!
    Checking <function strReverseR at 0x043186F0>('testing123')... Error has wrong value '321gnitset', expected '321gnitest'!
    Checking <function strReverseR at 0x043186F0>('a')... Error has wrong value 'a', expected 'b'!
    Checking <function strReverseR at 0x043186F0>('CIS 210')... Error has wrong value '012 SIC', expected '012 SIC#'!

    Checking <function strReverseI at 0x043187C8>('')... its value '' is correct!
    Checking <function strReverseI at 0x043187C8>('a')... its value 'a' is correct!
    Checking <function strReverseI at 0x043187C8>('aaaa')... its value 'aaaa' is correct!
    Checking <function strReverseI at 0x043187C8>('abc')... its value 'cba' is correct!
    Checking <function strReverseI at 0x043187C8>('hello')... its value 'olleh' is correct!
    Checking <function strReverseI at 0x043187C8>('racecar')... its value 'racecar' is correct!
    Checking <function strReverseI at 0x043187C8>('testing123')... Error has wrong value '321gnitset', expected '321gnitest'!
    Checking <function strReverseI at 0x043187C8>('a')... Error has wrong value 'a', expected 'b'!
    Checking <function strReverseI at 0x043187C8>('CIS 210')... Error has wrong value '012 SIC', expected '012 SIC#'!    test_reverse(p5.strReverseR)
    '''
    test_reverse(p5.strReverseR)
    print()
    test_reverse(p5.strReverseI)
    return None

main()
