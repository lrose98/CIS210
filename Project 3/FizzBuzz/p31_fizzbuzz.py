''' 
CIS 210 FIZZBUZZ
Fall 2018: Project 3
Author: Lillie Rose

Credits: N/A

Create the function Fizzbuzz, based off of the activity we did in class
the first week
'''

def fb(number):
    ''' (number) -> number, string
    Function counts from 1 to the argument inputted. However, every multiple of
    three 'fizz' is outputted. Every multiple of five 'buzz' is outputted. Every
    'three' and 'five' multiple, 'fizzbuzz' is outputted. Prints 'Game over!' at
    the end. Returns None.
            #Examples of use:
    >>>fb(5)
    1
    2
    fizz
    4
    buzz
    Game over!
    >>>fb(6)
    1
    2
    fizz
    4
    buzz
    fizz
    Game over!
    '''
    count = 1
    for _ in range(number):
        three = count % 3
        five = count % 5
        if three == 0 and five == 0:
            print('fizzbuzz')
        elif three == 0:
            print('fizz')
        elif five == 0:
            print('buzz')
        else:
            print(count)
        count +=1
    print('Game over!')
    return None
