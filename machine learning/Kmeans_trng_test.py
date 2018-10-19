#plotly = False
try:
    import math
    import random
    import plotly
    from plotly.graph_objs import Scatter, Scatter3d, Layout
    print("import ok")
except ImportError:
    print ("INFO: Plotly is not installed, plots will not be generated.")

class Point(object):
    def __init__(self, coords):
        self.coords = coords
        self.n = len(coords)
    def __str__(self):
        return str(self.coords)

print("Point class ok")
class Cluster(object):
    def __init__(self, points):
        if len(points) == 0:
            raise Exception("ERROR: empty cluster")
        self.points = points
        self.n = points[0].n
        for p in points:
            if p.n != self.n:
                raise Exception("ERROR: inconsistent dimensions")
        self.centroid = self.calculateCentroid()

    def __str__(self):
        return str(self.points)

    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        if len(self.points) == 0:
            return 0
        self.centroid = self.calculateCentroid()
        shift = getDistance(old_centroid, self.centroid)
        return shift
    def calculateCentroid(self):
        numPoints = len(self.points)
        coords = [p.coords for p in self.points]
        unzipped = zip(*coords)
        centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]
        return Point(centroid_coords)

    def getTotalDistance(self):
        sumOfDistances = 0.0
        for p in self.points:
            sumOfDistances += getDistance(p, self.centroid)
        return sumOfDistances


def getDistance(a, b):
    if a.n != b.n:
        raise Exception("ERROR: non comparable points")
    accumulatedDifference = 0.0
    for i in range(a.n):
        squareDifference = pow((a.coords[i]-b.coords[i]), 2)
        accumulatedDifference += squareDifference
    return accumulatedDifference

def makeRandomPoint(n, lower, upper):
    p = Point([random.uniform(lower, upper) for _ in range(n)])
    return p
def calculateError(clusters):
    accumulatedDistances = 0
    num_points = 0
    for cluster in clusters:
        num_points += len(cluster.points)
        accumulatedDistances += cluster.getTotalDistance()

    error = accumulatedDistances / num_points
    return error

def kmeans(points, k, cutoff):
    initial_centroids = random.sample(points, k)
    clusters = [Cluster([p]) for p in initial_centroids]
    #print("clusters:",list(clusters))
    loopCounter = 0
    while True:
        # Create a list of lists to hold the points in each cluster
        lists = [[] for _ in clusters]
        clusterCount = len(clusters)
        loopCounter += 1
        # For every point in the dataset ...
        for p in points:
            # Get the distance between that point and the centroid of the first
            # cluster.
            smallest_distance = getDistance(p, clusters[0].centroid)

            # Set the cluster this point belongs to
            clusterIndex = 0

            # For the remainder of the clusters ...
            for i in range(1, clusterCount):
                # calculate the distance of that point to each other cluster's
                # centroid.
                distance = getDistance(p, clusters[i].centroid)
                # If it's closer to that cluster's centroid update what we
                # think the smallest distance is
                if distance < smallest_distance:
                    smallest_distance = distance
                    clusterIndex = i
            # After finding the cluster the smallest distance away
            # set the point to belong to that cluster
            lists[clusterIndex].append(p)

        # Set our biggest_shift to zero for this iteration
        biggest_shift = 0.0

        # For each cluster ...
        for i in range(clusterCount):
            # Calculate how far the centroid moved in this iteration
            shift = clusters[i].update(lists[i])
            # Keep track of the largest move from all cluster centroid updates
            biggest_shift = max(biggest_shift, shift)

        # Remove empty clusters
        clusters = [c for c in clusters if len(c.points) != 0]

        # If the centroids have stopped moving much, say we're done!
        if biggest_shift < cutoff:
            print ("Converged after %s iterations" % loopCounter)
            break
    return clusters

def iterative_kmeans(points, num_clusters, cutoff, iteration_count):
    print ("Running K-means %d times to find best clusters ..." % iteration_count)
    candidate_clusters = []
    errors = []
    for _ in range(iteration_count):
        clusters = kmeans(points, num_clusters, cutoff)
        error = calculateError(clusters)
        candidate_clusters.append(clusters)
        errors.append(error)

    highest_error = max(errors)
    lowest_error = min(errors)
    print ("Lowest error found: %.2f (Highest: %.2f)" % (
        lowest_error,
        highest_error
    ))
    ind_of_lowest_error = errors.index(lowest_error)
    best_clusters = candidate_clusters[ind_of_lowest_error]

    return best_clusters

def unsupervised():
    num_points = 20
    dimensions = 2
    lower = 0
    upper = 200
    num_clusters = 3
    cutoff = 0.2
    points = [
        makeRandomPoint(dimensions, lower, upper) for i in range(num_points)#xrange
    ]
    print("points:",type(points))
    # Cluster those data!
    iteration_count = 20
    best_clusters = iterative_kmeans(
        points,
        num_clusters,
        cutoff,
        iteration_count
    )
    # Print our best clusters
    for i, c in enumerate(best_clusters):
        for p in c.points:
            print (" Cluster: ", i, "\t Point :", p)
unsupervised()




