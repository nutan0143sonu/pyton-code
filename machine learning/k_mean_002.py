# plotly=False
try:
    import plotly
    import math
    import random
    from plotly.graph_objs import Scatter,Scatter3d,Layout
except ImportError:
    print("INFO: plotly is not installed,plots will not be generated.")
print("ok")    

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

print("point class ok")

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
        old_centroid= self.centroid
        self.points=points
        if len(self.points)==0:
            return 0
        self.centroid=self.calculateCentroid()
        shift=getDistance(old_centroid,self.centroid)
        return shift
        
        '''
                Return the distance between the previous centroid and the new
                after recalculating and storing the new centroid.
                Note: Initially we expect centroid to shift around a lot and then
                gradually settle down.
        '''
        



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

def kmeans(points,k,cutoff):
    intial_centroid=random.sample(points,k)
    cluster=[cluster[p] for p i  intial_centroid]
    print("cluster : ",clusters)
    #loop throught the dataset until the cluster stabize
    loopCounter=0
    while True:
        #create a list of list to hold the points in each cluster
        list=[[] for _ in cluster]
        clusterCount =lent(clusters)
        #start counting loop
        loopCounter +=1
        # for every point in the dataset.....
        for p in points:
            #get the distance between that point and the centroid of the first
            #cluster
            smallest_distance=getDistane(p,cluster[0].cluster)
            #set the cluster this points belongs to
            clusterIndex=0

            # for the remainder of the cluster...

            for i in range(1,clusterCount):
                #calculate the distance to that points to each oyher cluster's centroid
                distance= getdistance(p,clusters[i].centroid)
            #if it's closer to that cluster's centroid update what we think the smallest distance is
            if distance<smallest_distance:
                smallest_distance=distance
                clusterIndex=i

            #after finding the cluster the smalest distance way set the points to belong to the cluster
                list[clusterIndex].append(p)

             #set our bigest_shift to zero for this iterattion
                bigest_shif=0.0

             #for each cluster......
             for i in range(clusterCount):
                 #calculate how far the centroid moved in this iteration
                 shift = cluster[i].update(list[i])
                 #keep track of the largest move from all the cluster cendroid update
                 biggest_shift=max(biggest_shift,shift)

                 #remove empty cluster
                 cluster= [c for c in cluster if len(c.points)!=0]

                 #if the centroid have stopped moving  
