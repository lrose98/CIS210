'''
CIS 210 Fall 1018
Project 2-2: FApproximate Square Root
Compare the Babylonian square root method with the math lib function

Author: Lillie Rose

Credits:Joey Valko Web Tunings(Youtube Video, https://www.youtube.com/watch?v=raLWyVq98NU
'''

import math
import string

def mysqrt(n,k):
    ''' (number, number) -> float
    Using the Babylonian method, return the approximate square root of
    a number (n). The return depends on how many times the process is
    repeated (k)
            #Examples of use:
    >>> mysqrt(25, 5)
    5.000023178253949
    >>> mysqrt(100, 10)
    10.0
    >>> mysqrt(10000, 11)
    100.0
    '''
    x = n
    for _ in range(k):
        x = .5 * (x + (n/x))
    return x


    
def sqrt_compare(num, iterations):
    ''' (number, number) -> string, float
    Sqaure root comparison, with the Babylonian method and the math lib method.
    Prints out multiple strings detailing each result and the percent error.
            #Examples of use:
    >>> sqrt_compare(25, 5)
    For using 25 using 5 iterations:
    mysqrt value is: 5.000023178253949
    math lib sqrt value is: 5.0
    This is a 0.0 percent error
    >>> sqrt_compare(100, 10)
    For using 100 using 10 iterations:
    mysqrt value is: 10.0
    math lib sqrt value is: 10.0
    This is a 0.0 percent error
    >>> sqrt_compare(10000, 11)
    For using 10000 using 11 iterations:
    mysqrt value is: 100.0
    math lib sqrt value is: 100.0
    This is a 0.0 percent error
    '''
    my = mysqrt(num, iterations)
    lib = math.sqrt(num)
    error= my - lib

    if(error < 0):
        error = error * -1
        error = round(error, 3)
    else:
        error = round(error, 3)
    
    print("For using", num, "using", iterations, "iterations:")
    print("mysqrt value is:", my)
    print("math lib sqrt value is:", lib)
    print("This is a", error, "percent error")

def main():
    '''Square root comparison program driver'''
    sqrt_compare(25, 5)
    sqrt_compare(25, 10)
    sqrt_compare(100, 10)
    sqrt_compare(625, 10)
    sqrt_compare(10000, 8)
    sqrt_compare(10000, 10)
    sqrt_compare(10000, 11)
    return None
