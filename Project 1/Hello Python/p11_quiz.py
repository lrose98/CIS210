''' 
CIS 210 STYLE
Fall 2018: Project 1
Author: Lillie Rose

Credits: Anisha Malynur (Help Hours)

Add docstrings to Python functions that implement quiz 1 pseudocode.
(See p11_cricket for examples of functions with docstrings.)
'''

def q1(onTime, absent):
    ''' (bool, bool) -> str
    Return string based on the the inital varibale. There are three
    possible outputs. onTime and absent values have specific returns,
    while any other string returns the same value.
            #Examples of use
    >>> q1(onTime)
    'Hello!'
    >>> q1 (absent)
    'Is anyone there?'
    >>> q1 (late)
    'Better late than never.'
    '''
    if onTime:
        return('Hello!')
    elif absent:
        return('Is anyone there?')
    else:
        return('Better late than never.')

def q2(age, salary):
    ''' (int) -> bool
    Return is true or flase. Function decides whether or not a person is
    a dependent based on the age and salary. To be a dependent child, the
    person must be under the age of 18 and not make 10,000 or more a year
            #Examples of use
    >>> q2(17, 9999)
    True
    >>> q2(18, 4)
    False
    >>> q2(14, 10001)
    True
    '''
    return (age < 18) and (salary < 10000)

def q3():
    ''' ( ) -> int
    Return will always be 6. Function evaluates the variables p and q, which are
    valued at p=1 and q=2. Since p has a lesser value than 2 but q is not greater than
    4, the result is changed from being equal to 4 to being equal to 6. Any argument added
    will result in an error.
            #Examples of use:
    >>> q3()
    6
    >>> q3(3)
    'TypeError: q6() takes 0 positional arguments but 1 was given'
    '''
    p = 1
    q = 2
    result = 4
    if p < q:
        if q > 4:
            result = 5
        else:
            result = 6

    return result

def q4(balance, deposit): 
    ''' (int) -> int
    Return the balance after ten deposits are added to the
    inital balance. The count variable aids the While loop with
    each stage of depositing.
            #Examples of use
    >>> q4(5, 3)
    35
    >>> q4(7, 21)
    217
    >>> q4(0, 1)
    10
    '''
    count = 0
    while count < 10:
        balance = balance + deposit
        count += 1

    return balance

def q5(nums): 
    '''  ([int]) -> int
    Return is the anount of non-negative numbers in a list of numbers.
            #Examples of use:
    >>>q5([1, 2 , -1)
    2
    >>>q5([-3, -3, -2])
    0
    >>>q5([-7, 0, 0])
    2
    '''
    result = 0
    i = 0
    while i < len(nums):
        if nums[i] >= 0:
            result += 1

        i += 1

    return result

def q6(): 
    ''' ( ) -> 
    The value of p is doubled until i reaches 2, the return is p. However,
    since the loop resets i to 1, the loop will infinetly increase p and never
    return anything. This function takes no arguments
            #Examples of use:
    >>> q6()

    >>> q6(3)
    'TypeError: q6() takes 0 positional arguments but 1 was given'
    '''
    i = 0
    p = 1
    while i < 4:
        i = 1
        p = p * 2
        i += 1

    return p



