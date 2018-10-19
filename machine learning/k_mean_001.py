import math
import random
#classes
class Points(object):
    '''
      A point in n dimentional space
    '''

    def __init__(self,coords):
        '''coords- A list of values ,one per dimention'''

        self.coords=coords
        self.n=len(coords)
    def __repr__(self):# this is same as __str__ and it return value instead of address by printing object of class
        return str(self.coords)

#cluster class
    class Cluster(object):
        def __init__(self,points):
            if len(points)==0:
                raise Exception("Error: empty cluster")# when we want to create own exception then we use raise keywords
            #the point that belong to the cluster
            self.point=points
            #The dimentionality of the points in this cluster
            self.n=points[0].n
            #Assert  that all points are of the same dimentionality
            for p in points:
                if p!=self.n:
                    raise Exception("Error: inconsistent dimention")
            #set up the initial cetroid(this is usally based off one points)
            self.centroid=self.calculateCentroid()
        def __str__(self):
            return str(self.points)
        def update(self,points):
            '''
                Return the distance between the previous centroid and the new
                after recalculating and storing the new centroid.
                Note: Initially we expect centroid to shift around a lot and then
                gradually settle down.
            '''
            old_centroid= self.centroid
            self.points=points
            if len(self.points)==0:
                return 0
            self.centroid=self.calculateCentroid()
            shift=getDistance(old_centroid,self.centroid)
            return shift



        def calculateCentroid(self):
            numPoints=len(self.points)
            #Get a list of all coordinates in this cluster
            coords=[p.coords for p in self.points]
            #Reformat that so all x's  are together ,all y's etc
            unzipped=zip(*coords)
            #calculate the mean for eac dimension
            centroid_coords=[math.fsum(sList)/numPoints for dList in unzipped]
            return Points(centroid_coords)
        def getTotalDistance(self):
            sumOfDistance=0.0
            for p in self.points:
                sumOfDistance +=getDistance(p,self.centroid)
            return sumOfDistance
        

def getDistance(a,b):
    if a.n!=b.n:
        raise Exception("Error: non comparable points")

    accumulatedDifference=0.0
    for i in range(a.n):
        squareDifference=pow((a.coords[i]-b.coords[i]),2)
        accumulatedDifference +=squareDifference

    return accumulatedDifference
def makeRandomPoint(n,lower,upper):
    p=points([random.uniform(lower,upper)for _ in range(n)])# _ is used for private variable and __ is strictly private
    return p


def calculateError(cluster):
    accumulatedDistance=0
    num_points=0
    for cluster in clusters:
        num_points +=len(cluster.points)
        accumulatedDistance +=cluster.getTotalDistancre()

    error=accumulatedDistance/num_points
    return error


            
