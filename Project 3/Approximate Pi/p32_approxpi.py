'''
Approximating pi.  CIS 210 F18 Project 3-2
Starter Code for showMontePi

Author: CIS 210

Credits: Based on code on Chapter 2.6 Miller and Ranum text. 

Approximate pi using a Monte Carlo simulation.

'''
import random
import math

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

    
def montePi(numDarts):
    ''' (number) -> float
    Approximated Pi using the Monte Carlo simulation. Functions calls isInCircle()
    as apart of the loop. Returns the estimated Pi. Estimations subjected to be
    different with every simulation
    >>>montePi(1000)
    3.196
    >>>montePi(10000)
    3.1496
    >>>montePi(100000)
    3.13712
    '''
    inCircle = 0

    r = 1 #assume that the radius of the circle is 1
    

    for _ in range(numDarts):
        x = random.random()
        y = random.random()
        
        
        if isInCircle(x, y, r) == True:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4

    return pi

def main():
    ''' () -> float, float, float
    Calls montePi four times, increasing the number of Darts by 10x. Prints
    out the results.
    #Note: results will be different with each time
            #Examples of use:
    >>>main()
    3.214
    3.196
    3.1496
    3.13712
    '''
    print(montePi(100))
    print(montePi(1000))
    print(montePi(10000))
    print(montePi(100000))

    
    return None

main()

def altisInCircle(xx, yy, rr):
    ''' (float, floar, float) -> bool
    An alternative way to write isInCircle. Still returns a boolean based on the
    coordinates xx and yy
    >>>isInCircle(3, .5, 1)
    False
    >>>isInCircle(.3, .7, 1)
    True
    >>>isInCircle(.5, 1, 1)
    False
    '''
    dd = 0
    if xx < r:
        dd = dd + 1

    if yy < r:
        dd = dd + 1


    if dd == 2:
        return True
    else:
        return False



    
