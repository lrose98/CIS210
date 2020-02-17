'''
CIS 210 Fall 2018
Project 5-2: String Reverse

Author: Lillie Rose

Credits: N/A
'''
import doctest

def stringReverseR(S):
    ''' (str) -> str
    Using a recursive function, return a string backwards.
                #Examples of use:
    >>> stringReverseR('main')
    'niam'
    >>> stringReverseR('asdf')
    'fdsa'
    >>> stringReverseR('check')
    'kcehc'
    '''
    if len(S) == 0:
        return ''
    else:
        char= len(S) -1
        return S[char] + stringReverseR(S[:-1])

    
def stringReverseI(S):
    ''' (str) -> str
    Using a recursive function, return a string backwards.
            #Examples of use:
    >>> stringReverseI('main')
    'niam'
    >>> stringReverseI('asdf')
    'fdsa'
    >>> stringReverseI('check')
    'kcehc'
    '''
    num= int(len(S)) -1
    reverse= ""
    while num >= 0:
        reverse += S[num]
        num = num - 1
    return reverse

def main(S= 'reverse'):
    ''' () -> str, None
    Reverse a string and then reverse the reversed string using
    stringReverse(R) and stringReverse(I)
                #Examples of use:
    >>> main()
    Enter a string: reverse
    Using a recursive function, assd backwards is esrever
    Using a iterative function, dssa backwards is reverse
    '''
    S= input("Enter a string: ")
    if S == '':
        S= 'reverse'

    revR= stringReverseR(S)
    print("Using a recursive function, " + S + " backwards is " + revR)
    revI= stringReverseI(revR)
    print("Using a iterative function, " + revR + " backwards is " + revI)
    return None


print(doctest.testmod())
