'''
CIS 210 Fall 2018
Project 2-3: Draw Flower
Draw a flower using geometric shapes

Author: Lillie Rose, Joey Valko

Credits: Web Tunings(Youtube Video, https://www.youtube.com/watch?v=raLWyVq98NU
'''
from turtle import *
import math

def drawFlower():
    ''' ( )  -> Line + Triangle graphic
    Draws the stem of the flower along with two triangular pedals.
    Should be used in conjunction with drawPolygon()
            #Example of use:
    >>>drawFlower()
    Graphic
            
    '''
    penup()                     #penup first, just in case
    setpos(0, -20)
    pendown()
    setpos(0, -200)             #this is the stem
    ycord = -100
    
    for _ in range(2):          #this is the two pedals
        penup()
        setpos(0, ycord)
        pendown()        
        right(90)
        for i in range(3):
            forward(40)
            right(120)
        ycord = ycord - 60
        right(90)
    penup()

def drawPolygon(numSquares):
    ''' (int) -> Polygon graphic
    A number of squares will be drawn, strarting from the same point but the
    degree is of the starting line is rotated after every square
            #Example of use:
    >>>drawPolygon(5)
    Five square graphic
    >>>drawPolygon(25)
    Twenty-five square graphic
    '''
    penup()                     #penup first, just in case
    setpos(0, -20)
    degrees= 360 / numSquares
    penup()
    setpos(0,0)
    repeat = 1
    
    while(repeat <= numSquares):
        for _ in range (4):
            pendown()
            forward(60)
            right(90)
        penup()
        right(degrees)
        repeat+=1

def main():
    '''
    Calls drawFlower() for the stem and calls drawPolygon(25) to make a 25
    petal flower. The petals are purple with outlined in yellow and the
    stem is turqoised outlined in green
            #Examples of use:
    >>>main()
    Flower graphic
    '''
    speed(10)
    pendown()
    color("#FFDB58", "#CCCCFF")
    begin_fill()
    drawPolygon(25)
    end_fill()
    
    color("#228B22", "#40E0D0")
    begin_fill()
    drawFlower()
    end_fill()

def art_show():
    ''' ( ) -> Graphic
    Draws 11 fence posts
            #Example of use:
    >>> art_show()
    fancy fence
    '''

    penup()                      #penup first, just in case
    setpos(-440, -200)           #starting coordinates
    color("#717080", "#786E6C" ) 
    speed(10)
    begin_fill()
    pendown()
    
    for _ in range(11):
        right(270)
        forward(360)
        right(30)
        for i in range(3):
            forward(80)
            right(120)
        right(330)
        backward(360)
        right(90)
        forward(80)
    end_fill()
    right(270)
    forward(360)                #last line of fence
    penup()
    setpos(0,0)
    penup()
    right(90)
