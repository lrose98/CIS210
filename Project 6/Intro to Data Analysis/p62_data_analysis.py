'''
Project 6-2: Project Analysis
Understand, implement, and revise data analysis and visualization functions.
Author:Lillie Rose

Credits: Stack Overflow threads
'''
import doctest

def mean(alist):
    ''' (list) -> float
    Returns the average of a list
                #Examples of use:
    >>> mean([1, 2, 3])
    2.0
    >>> mean([88, 34, 17])
    46.333333333333336
    >>> mean([123, 543, 28])
    231.33333333333334
    '''
    mean= sum(alist)/ len(alist)
    return mean

def median(alist):
    '''
    Returns the sequentially middle number. If list is even, the returned number
    is the middle of the two middle number
    >>> median([2, 5, 6, 7, 7, 4, 2, 8, 9, 1])
    5.5
    >>> median([3, 56, 23, 67, 31, 77])
    43.5
    >>> median([435, 657, 293, 111, 239, 748, 839, 271])
    364.0
    '''
    copylist= alist[:] #make a copy using slice operator
    copylist.sort()
    if len(copylist)%2 == 0:
        rightmid= len(copylist)//2
        leftmid= rightmid - 1
        median= (copylist[leftmid] + copylist[rightmid])/2
    else:
        mid= len(copylist)//2
        median= copylist[mid]
    return median

def genFrequencyTable(alist):
    '''
    Given the number list, returns numerical list of all numbers
    used, along with the number of times it was used.
    >>> genFrequencyTable([1, 2, 2, 3, 3, 3])
    {1: 1, 2: 2, 3: 3}
    >>> genFrequencyTable([1, 2, 2, 6, 3, 3, 7, 3, 4, 6])
    {1: 1, 2: 2, 3: 3, 4: 1, 6: 2, 7: 1}
    >>> genFrequencyTable([33, 22, 54, 31, 64, 42, 593, 283])
    {22: 1, 31: 1, 33: 1, 42: 1, 54: 1, 64: 1, 283: 1, 593: 1}
    '''
    countdict= {}
    for item in alist:
        if item in countdict:
            countdict[item]= countdict[item]+1
        else:
            countdict[item]= 1
            
    itemlist= list(countdict.keys())
    itemlist.sort()

    genFlist= {}
    for item in itemlist:
        genFlist[item]= countdict[item]
    return genFlist

def mode(alist):
    '''
    Returns the number that is most frequent in list. If multiple numbers have the
    same frequency, returns all.
    >>> mode([12, 42, 27, 93, 74, 33, 12])
    [12]
    >>> mode([1, 1, 1, 2, 2, 2, 4])
    [1, 2]
    >>> mode([12, 53, 23, 75, 49, 33])
    [12, 23, 33, 49, 53, 75]
    '''
    countdict= genFrequencyTable(alist)
    
    itemlist= countdict.values()
    maxcount= max(itemlist)

    modelist= []
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)

    return modelist

def frequencyTable(alist):
    '''
    Returns each number in the list with the number of times it is repeated in
    the list
    >>> frequencyTable([1, 2, 2, 3, 3, 3])
    ITEM FREQUENCY
    1         1
    2         2
    3         3
    >>> frequencyTable([43, 34, 52, 11, 34, 76, 43, 34])
    ITEM FREQUENCY
    11         1
    34         3
    43         2
    52         1
    76         1
    '''
    countdict= genFrequencyTable(alist)
    itemlist= list(countdict.keys())
    itemlist.sort()

    print("ITEM", "FREQUENCY")

    for item in itemlist:
        print(item, "       ", countdict[item])

    return None

def isEven(n):
    '''
    Returns true if number is even. Returns false if not.
    >>> isEven(3)
    False
    >>> isEven(4)
    True
    >>> isEven(1.2)
    False
    '''
    if n%2 == 0:
        return True
    else:
        return False

def main():
    '''
    Report the mean, median, and mode of equakes
                #Examples of use:
    >>> main()
    The mean for equakes is 3.780748663101608
    The median for equakes is 3.3
    The mode for equakes is [2.5]
    '''
    equakes= [5.3, 3.0, 2.6, 4.4, 2.9, 4.8, 4.3, 2.6, 2.9, 4.9, 2.5, 4.8, 4.2, 2.6, 4.8, 2.7, 5.0, 2.7, 2.8, 4.3, 3.1, 4.1, 2.8, 5.8, 2.5, 3.9, 4.8, 2.9, 2.5, 4.9, 5.0, 2.5, 3.2, 2.6, 2.7, 4.8, 4.1, 5.1, 4.7, 2.6, 2.9, 2.7, 3.3, 3.0, 4.4, 2.7, 5.7, 2.5, 5.1, 2.5, 4.4, 4.6, 5.7, 4.5, 4.7, 5.1, 2.9, 3.3, 2.7, 2.8, 2.9, 2.6, 5.3, 6.0, 3.0, 5.3, 2.7, 4.3, 5.4, 4.4, 2.6, 2.8, 4.4, 4.3, 4.7, 3.3, 4.0, 2.5, 4.9, 4.9, 2.5, 4.8, 3.1, 4.9, 4.4, 6.6, 3.3, 2.5, 5.0, 4.8, 2.5, 4.2, 4.5, 2.6, 4.0, 3.3, 3.1, 2.6, 2.7, 2.9, 2.7, 2.9, 3.3, 2.8, 3.1, 2.5, 4.3, 3.2, 4.6, 2.8, 4.8, 5.1, 2.7, 2.6, 3.1, 2.9, 4.2, 4.8, 2.5, 4.5, 4.5, 2.8, 4.7, 4.6, 4.6, 5.1, 4.2, 2.8, 2.5, 4.5, 4.6, 2.6, 5.0, 2.8, 2.9, 2.7, 3.1, 2.6, 2.5, 3.2, 3.2, 5.2, 2.8, 3.2, 2.6, 5.3, 5.5, 2.7, 5.2, 6.4, 4.2, 3.1, 2.8, 4.5, 2.9, 3.1, 4.3, 4.9, 5.2, 2.6, 6.7, 2.7, 4.9, 3.0, 4.9, 4.7, 2.6, 4.6, 2.5, 3.2, 2.7, 6.2, 4.0, 4.6, 4.9, 2.5, 5.1, 3.3, 2.5, 4.7, 2.5, 4.1, 3.1, 4.6, 2.8, 3.1, 6.3]
    print('The mean for equakes is {}'.format(mean(equakes)))
    print('The median for equakes is {}'.format(median(equakes)))
    print('The mode for equakes is {}'.format(mode(equakes)))
    return None

main()

print(doctest.testmod())
