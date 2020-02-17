'''
Project 6-1: Automated Testing
Write a function to test the string reverse functions from Project 5-2.
Author:Lillie Rose

Credits: Stack Overflow threads
'''

import doctest

def isMemberI(aseq, target):
    ''' (tuple/str, str/num) -> bool
    Return if target arguments is in aseq using an irerative approach.
                #Examples of use:
    >>> isMemberI((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberI((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberI('aeiou', 'i')
    True
    >>> isMemberI('aeiou', 'y')
    False
    >>> isMemberI((1, 3, 5, 7), 4) #even number of items - False
    False
    >>> isMemberI((23, 24, 25, 26, 27), 5) #odd number of items - False
    False
    >>> isMemberI((0, 1, 4, 5, 6, 8), 4) # even number of items - True
    True
    >>> isMemberI((0, 1, 2, 3, 4, 5, 6), 3) # odd number of items - True
    True
    >>> isMemberI((1, 3), 1) # target is first (zeroth) item
    True
    >>> isMemberI((2, 10), 10) # target is last item
    True
    >>> isMemberI((99, 100), 101) # short sequence - False
    False
    >>> isMemberI((42,), 42) # one item sequence - True
    True
    >>> isMemberI((43,), 44) # one item sequence - False
    False
    >>> isMemberI((), 99) # empty sequence
    False
    '''
    midp= (len(aseq)//2)
    isit= False
    loop= 0

    if len(aseq) <= 2: #binary search would not accurately analyze 1 len and 2 len tuples
        for i in range(len(aseq)):
            if target == aseq[i]:
                isit = True
            else:
                pass
    else:
        while (isit != True) and (0 < midp < len(aseq)) and (loop < len(aseq)):
            if target == aseq[midp]:
                #print(midp, aseq[midp], "eq")
                isit= True
            elif target < aseq[midp]:
                #print(midp, aseq[midp], "down")
                midp= midp - 1
                loop= loop + 1
            elif target > aseq[midp]:
                #print(midp, aseq[midp], "up")
                midp= midp +1
                loop= loop + 1
    return isit
   
def isMemberR(aseq, target):
    '''  (tuple/str, str/num) -> bool
    Return if target arguments is in aseq using an recursive approach.
                #Examples of use:
    >>> isMemberR((1, 2, 3, 3, 4), 4)
    True
    >>> isMemberR((1, 2, 3, 3, 4), 2)
    True
    >>> isMemberR('aeiou', 'i')
    True
    >>> isMemberR('aeiou', 'y')
    False
    >>> isMemberR((1, 3, 5, 7), 4) #even number of items - False
    False
    >>> isMemberR((23, 24, 25, 26, 27), 5) #odd number of items - False
    False
    >>> isMemberR((0, 1, 4, 5, 6, 8), 4) # even number of items - True
    True
    >>> isMemberR((0, 1, 2, 3, 4, 5, 6), 3) # odd number of items - True
    True
    >>> isMemberR((1, 3), 1) # target is first (zeroth) item
    True
    >>> isMemberR((2, 10), 10) # target is last item
    True
    >>> isMemberR((99, 100), 101) # short sequence - False
    False
    >>> isMemberR((42,), 42) # one item sequence - True
    True
    >>> isMemberR((43,), 44) # one item sequence - False
    False
    >>> isMemberR((), 99) # empty sequence
    False
    '''
    count= len(aseq)
    if count == 0:
        return False
    else:
        midp= (count//2)
        if target == aseq[midp]:
            #print(midp, aseq[midp], "eq")
            return True
        elif target < aseq[midp]:
            #print(midp, aseq[midp], "down")
            return isMemberR(aseq[:midp], target)      
        elif target > aseq[midp]:
            #print(midp, aseq[midp], "up")
            return isMemberR(aseq[midp+1:], target)
    
def bintest(isMemberX):
    ''' (func) -> None
    Test the isMember functions with the arguments given in the p91 project description.
                #Examples of use
    >>> bintest(isMemberR)
    Now checking function isMemberR...
    Checking isMemberR((1, 2, 3, 3, 4), 4)... True is correct!
    Checking isMemberR((1, 2, 3, 3, 4), 2)... True is correct!
    Checking isMemberR('aeiou', 'i')... True is correct!
    Checking isMemberR('aeiou', 'y')... False is correct!
    Checking isMemberR((1, 3, 5, 7), 4)... False is correct!
    Checking isMemberR((23, 24, 25, 26, 27), 5)... False is correct!
    Checking isMemberR((0, 1, 4, 5, 6, 8), 4)... True is correct!
    Checking isMemberR((0, 1, 2, 3, 4, 5, 6), 3)... True is correct!
    Checking isMemberR((1, 3), 1)... True is correct!
    Checking isMemberR((2, 10), 10)... True is correct!
    Checking isMemberR((99, 100), 101)... False is correct!
    Checking isMemberR((42,), 42)... True is correct!
    Checking isMemberR((43,), 44)... False is correct!
    Checking isMemberR((), 99)... False is correct!
    >>> bintest(isMemberI)
    Now checking function isMemberI...
    Checking isMemberI((1, 2, 3, 3, 4), 4)... True is correct!
    Checking isMemberI((1, 2, 3, 3, 4), 2)... True is correct!
    Checking isMemberI('aeiou', 'i')... True is correct!
    Checking isMemberI('aeiou', 'y')... False is correct!
    Checking isMemberI((1, 3, 5, 7), 4)... False is correct!
    Checking isMemberI((23, 24, 25, 26, 27), 5)... False is correct!
    Checking isMemberI((0, 1, 4, 5, 6, 8), 4)... True is correct!
    Checking isMemberI((0, 1, 2, 3, 4, 5, 6), 3)... True is correct!
    Checking isMemberI((1, 3), 1)... True is correct!
    Checking isMemberI((2, 10), 10)... True is correct!
    Checking isMemberI((99, 100), 101)... False is correct!
    Checking isMemberI((42,), 42)... True is correct!
    Checking isMemberI((43,), 44)... False is correct!
    Checking isMemberI((), 99)... False is correct!
    '''
    print('Now checking function {}...'.format(isMemberX.__name__))
    functlist= [((1, 2, 3, 3, 4), 4), ((1, 2, 3, 3, 4), 2), ('aeiou', 'i'), ('aeiou', 'y'), ((1, 3, 5, 7), 4), ((23, 24, 25, 26, 27), 5), ((0, 1, 4, 5, 6, 8), 4), ((0, 1, 2, 3, 4, 5, 6), 3), ((1, 3), 1), ((2, 10), 10), ((99, 100), 101), ((42,), 42), ((43,), 44), ((), 99)]
    funcreturn= [True, True, True, False, False, False, True, True, True, True, False, True, False, False]
    for funct in range(len(functlist)):
        arg= functlist[funct]
        arg= list(arg)
        arg1= arg[0]
        arg2= arg[1]

        #because 3 & 4 are strings
        if funct == 2 or funct == 3:
            arg1= str(arg1)
            arg2= str(arg2)
            if isMemberX(arg1, arg2) == funcreturn[funct]:
                print("Checking {}({}, {})... {} is correct!".format(isMemberX.__name__, '\'' + arg1 + '\'',  '\'' + arg2 + '\'', isMemberX(arg1, arg2)))
            else:
                print('wrong')
        else:
            if isMemberX(arg1, arg2) == funcreturn[funct]:
                print("Checking {}({}, {})... {} is correct!".format(isMemberX.__name__, arg1, arg2, isMemberX(arg1, arg2)))
            else:
                print(isMemberX(arg1, arg2))

    return None

def main():
    ''' () -> None
    Call bintest to test isMemberI and isMemberR
                #Examples of use:
    > main
    .....
    '''
    bintest(isMemberR)
    bintest(isMemberI)
    return None

main()

#print(doctest.testmod())

def optionalpoem ():
    ''' () -> None
    Print out three haiku's for extra credit.
    #I did three becuase haiku's are short and I wanted to show
    that I tried
                #Examples of use:
    >> optionalpoem()
    My contribution: 
     The keyboard clicks 
     every character has purpose 
     in the lines of code 

    T to B: 
     Editors translate 
     text into the binary 
     so it can understand 

    Solving: 
     Functions are questions 
     each problem has a solution, 
     sometimes multiple 
    
    '''
    print('My contribution: \n The keyboard clicks \n every character has purpose \n in the lines of code \n')
    print('T to B: \n Editors translate \n text into the binary \n so it can understand \n')
    print('Solving: \n Functions are questions \n each problem has a solution, \n sometimes multiple \n')

    return None
