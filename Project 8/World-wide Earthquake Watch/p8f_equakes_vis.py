'''
Project 8-1: Earthquake Visual
Visualize earthquake patterns based on their longitude and lattitude
Date: 11/19/18

Name: Lillie Rose
'''

import random
import turtle
import math

def readFile(filename):
    ''' (str) -> dict
    Return the longitude and latitude within an earthquakes file.
                #Examples of use:
    >> readFile('earthquakes.txt')
    {1: [lat, lon], ...}
    >> readFile(earthquakes.txt)
    NameError: earthquakes is not defined
    '''
    datafile = open(filename, "r")
    datadict = {}
    key = 0

    depth= datafile.readline()
    for aline in datafile:
        items = aline.split(',')
        key = key + 1
        lat= float(items[1])
        lon= float(items[2])
        datadict[key] = [lon, lat]

    return datadict

def euclidD(point1, point2): #240
    ''' (list, list) -> float
    Computing the Euclidean distance between two points
    (as stated by the book)
                #Examples of use:
    >>> euclidD([142.8358, -6.2147], [166.5962, -13.3911])
    24.820502112568153
    >>> euclidD([-186.2348, -66.666], [133,345, 0])
    520.9412184565932
    >>> euclidD([0, 0], [O, 2])
    Traceback (most recent call last):
      File "<pyshell#18>", line 1, in <module>
        euclidD([0, 0], [O, 2])
    NameError: name 'O' is not defined
    '''
    total= 0
    for index in range(len(point1)):
        diff = (point1[index]- point2[index]) ** 2
        total = total + diff
    euclidDistance = math.sqrt(total)

    return euclidDistance

def createCentroids(k, datadict): #248
    ''' (float, dict) -> list
    Return the number of valid Centroids
                #Examples of use:
    >>> createCentroids(5, datadict)
    [[-173.6463, -16.5296], [142.5704, 29.3187], [98.2153, 84.9401], [132.044, 30.7011], [-93.1019, 14.2914]]
    >>> createCentroids(8, datadict)
    [[44.9358, 36.1833], [45.7614, 35.0786], [99.6788, 84.8712], [145.6678, 43.1132], [98.4164, 0.6114], [125.1824, -0.2471], [-73.9789, -37.4492], [-161.0921, -62.7405]]
    
    '''
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1

    return centroids

def createClusters(k, centroids, datadict, repeats): #249
    ''' (num, list, dict, num) -> list
    Return the cluster areas within the list of lon/lat of earthquakes
    >> createClusters(6, [[166.5962, -13.3911], [-111.4155, 42.5629], [92.1222, 85.3247], [141.7711, 34.5757], [137.5681, 35.8637], [168.8509, -21.8262]], datadict, 7)
    [[1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 46, 47, 55, 58, 62, 65, 71], [45, 48, 51, 52, 53, 54, 56, 59, 60, 61, 63, 64, 67, 68, 69], [49, 70], [41, 44, 72], [17, 37, 42, 43, 50, 57, 66], [2, 8]]

    '''
    for apass in range(repeats):
        '''
        print("****PASS", apass, "****")
        '''
        clusters = []
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey], centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)
            
            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints= datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen

            centroids[clusterIndex] = sums
        ''' #comment out report
        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(datadict[key], end= "  ")
                print()
        '''

        return clusters
def eqDraw(k, eqDict, eqClusters):
    ''' (num, dict, list) -> Turtle graphics)
    Draws the points and clusters
                #Examples of use:
    >> eqDraw(5, datadict, clusters)
    Turtle graphics...
    'done analyzing'
    #click to exit
    '''
    turtle.speed(10)
    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(488, 266)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()

    colorlist = ["red", "green", "orange", "cyan", "yellow", "white", "black"]

    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in eqClusters[clusterIndex]:
            lon = eqDict[akey][0]
            lat= eqDict[akey][1]
            quakeT.goto(lon*wFactor, lat*hFactor)
            quakeT.dot()
    print('done analyzing')
    quakeWin.exitonclick()

    return None
    
def visualizeQuakes(k, r, dataFile): #k=6, r=7
    ''' (num, num, str) -> Turtle Graphics
    Visualize earthquake clusters by plotting them on a map
                #Examples of use:
    >> visualizeQuakes(6, 7, 'earthquakes.txt')
    Turtle graphics...
    >> visualizeQuakes(2, 6, 'earthquakes.txt')
    Turtle graphics...
    >> visualizeQuakes(7, 1, 'earthquakes.txt')
    Turtle graphics...
    '''
    datadict= readFile(dataFile)
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    eqDraw(k, datadict, clusters)

    return None


def main():
    '''
    Call visualizeQuakes and all other needed functions to plot lon/lat on
    a map
                #Examples of use:
    >> main()
    Turle graphics
    '''
    k=6
    r= 7
    dataFile= 'earthquakes.txt'

    visualizeQuakes(k, r, dataFile)

    return None

main()

def smallDataDict(fname):
    ''' (str) -> list
    Creates a smaller library of lon/lat for datadict
                #Examples of use:
    >> smallDataDict('earthquakes.txt')
    {1-73: [l,l]}
    '''
    datadict= readFile(fname)

    fdata= {}
    key = 1
    while key < 73:
        fdata[key] = datadict[key]
        key = key + 1
   

    return fdata

