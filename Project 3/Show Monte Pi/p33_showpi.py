'''
Approximating pi.  CIS 210 F18 Project 3-3
Starter Code for showMontePi

Author: CIS 210

Credits: Based on code on p.78 Miller and Ranum text.

Approximate pi using a Monte Carlo simulation.
Then add graphics to visualize simulation.
'''

from turtle import *
import math
import random

def isInCircle(x, y, r):
    ''' (float, floar, float) -> bool
    Given the radius, function returns whether the coordintes (x,y) fall
    into the cirlce. Returns Ture if yes, returns False if not.
                #Examples of use:
    >>>isInCircle(2, .4, 1)
    False
    >>>isInCircle(.3, .3, 1)
    True
    >>>isInCircle(.5, 1, 1)
    False
    '''
    d = math.sqrt(x**2 + y**2)
    
    if d <= r:
        return True
    else:
        return False
    
def drawBoard():
    ''' () -> Turtle graphics
    Draws a graph through Turtle Graphics, where each axes goes from -2 to
    2
            #Examples of use:
    >>>drawBoard()
    Turtle graphics
    '''
    # set up canvas and turtle
    # to animate the algorithm;
    # draw x, y axes
    # new drawBoard function will replace
    
    wn = Screen()
    wn.setworldcoordinates(-2, -2, 2, 2)

    speed(0); hideturtle()
    penup()

    goto(-1, 0)
    pendown()
    goto(1, 0)
    penup()
    goto(0, 1)
    pendown()
    goto(0, -1)
    penup()
    goto(0, -1)

    # pen should stay up for drawing darts

def reportPi(numDarts, approxPi):
    ''' (number, float) -> string (return None)
    Compare Monte Carlo approximation of Pi compated to the
    math lib. States the percent error between the two. returns
    None
            #Examples of use:
    >>>reportPi( 1000, 3.196)
    With 1000 iterations:
    My approximate value for pi is: 3.196
    The math lib value for pi is: 3.143
    This is a 0.053 percent error
    >>>eportPi( 1000, 3.213)
    With 1000 iterations:
    My approximate value for pi is: 3.213
    The math lib value for pi is: 3.143
    This is a 0.07 percent error
    >>>reportPi( 1000, 3.045)
    With 1000 iterations:
    My approximate value for pi is: 3.045
    The math lib value for pi is: 3.143
    This is a 0.098 percent error
    '''
    approx = approxPi
    pie = 22/7
    actual = round(22/7, 3) #the fraction of pi
    error = actual - approx

    if(error < 0):
        error = error * -1
        error = round(error, 3)
    else:
        error = round(error, 3)
        
    print("With", numDarts, "iterations:")
    print("My approximate value for pi is:", approx)
    print("The math lib value for pi is:", actual)
    print("This is a", error, "percent error")

    return None

def showMontePi(numDarts):
    ''' (number) -> Turtle graphics, str
    Calls drawBoard() to create graph for plotting. Plots random coordinates Calls isInCircle
    ans determines if dots are in the circle, with blue dots being inside the circle and red
    dots being out of it. At the end, it approximate value of PI. Calls report PI to compare,
    returns 0.
                #Examples of use:
    >>>showMontePi(1000)
    --turtle graphic--    
    With 1000 iterations:
    My approximate value for pi is: 3.196
    The math lib value for pi is: 3.143
    This is a 0.053 percent error
    >>>showMontePi(1000)
    --turtle graphic--    
    With 1000 iterations:
    My approximate value for pi is: 3.213
    The math lib value for pi is: 3.143
    This is a 0.07 percent error
    >>>showMontePi(1000)
    --turtle graphic--    
    With 1000 iterations:
    My approximate value for pi is: 3.045
    The math lib value for pi is: 3.143
    This is a 0.098 percent error
    '''
    clearscreen()
    speed('fastest')
    drawBoard()
    
    inCircleCt = 0

    # throw the darts and check whether
    # they landed on the dart board and
    # keep count of those that do   
    for i in range(numDarts):
        x = random.random()
        y = random.random()

    # Revise code to call new isInCircle function.
    # See Project 3-2 and 3-3 specifications.

        d = isInCircle(x, y, 1)

        # show the dart on the board
        if d == True:
            inCircleCt += 1
            color('blue')
        else:
            color('red')

        goto(x, y)
        dot()

    # calculate approximate pi
    approxPi = inCircleCt/numDarts * 4

    # ADD CODE HERE to compare approxPi to math.pi
    # call reportPi function to do this.
    # See Project 3-3 specification

    #wn.exitonclick()

    reportPi(numDarts, approxPi)

    return None

#add main function, too - definition and call
def main():
    ''' () -> turlte graphics, str
    Calls showMontePi(1000)
            #Examples of use:
    >>> main()
    --turtle graphic--    
    With 1000 iterations:
    My approximate value for pi is: 3.196
    The math lib value for pi is: 3.143
    This is a 0.053 percent error
    '''
    showMontePi(1000)

    return None

main()
