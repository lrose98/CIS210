'''                          # FILE HEADER
Python Variations
CIS 210 F18 Project 1

Author: Lillie Rose

Credits: Anisha Malynur (Help Hours)

Manipulate numbers based on the background of each
function.
'''

def convert(i, j, k):
    ''' (int, int, int) -> int
    Return a three digit number where k is the first digit, j is the
    second digit, and i is the third digit. All values of i, j, and k
    must be between 0-9.
            #Examples of use
    >>>convert(4, 7, 2)
    274
    >>>convert(12, 6, 4)
    "Error, numbers inputted are not non-negative single digit #'s. Try again"
    >>>convert(0, 2, 5)
    520
    '''
    i1 = i
    j1 = j * 10
    k1 = k * 100
    numb = i1 + j1 + k1

    #If/Else used to help ensure that i, j, and k are positive and 0-9
    if i >=0 and j >=0 and k >=0:
        if i <=9 and j <=9 and k <=9:
            return numb
        else:
            return 'Error, numbers inputted are not non-negative single digit #\'s. Try again'
    else:
        return 'Error, numbers inputted are not non-negative single digit #\'s. Try again'



def add_digits(n):
    ''' (int) -> int
    The input is a three digit number (n). The return is the sum
    of all the digits. If n is not a three digit number, the
    function asks the user to try again
                #Examples of use
    >>>add_digits(325)
    10
    >>>add_digits(473)
    14
    >>>add_digits(1024)
    'Input was not a three digit number. Please try again'
    '''
    if n > 99 and n < 1000:
        #XYZ get the value of X
        x1 = n // 100
        #XYZ get the value of Y
        y0 = n % 100
        y1 = y0 // 10
        #XYZ get the value of Z
        z1 = n %+ 10

        value = x1 + y1 + z1

        return value
    #else is used to differentiate non three digit numbers
    else:
        return "Input was not a three digit number. Please try again"

    
     
def profit(a):
    ''' (int) -> float
    a is equal to the number of attendees. The net_profit is calculated
    by the profit the movie theater gets from ticket sales (with $5 a
    ticket) and the cost of each show ($20 plus $0.5 for every attendee)
                #Examples of use
    >>> profit(5)
    2.5
    >>> profit(10)
    25.0
    >>> profit(2)
    -11.0
    '''
    pay = a * 5
    perAT = a * .5
    cost = 20 + perAT
    net_profit = pay - cost
    
    return net_profit
