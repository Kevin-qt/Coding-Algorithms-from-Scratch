import random
import math
import numpy as np

def pointsGenerator(n: int, scope: int, dim: int) -> dict:
    """Generate n random points in vector space"""
    points = dict()
    for i in range(1, n+1):
        points[i] = tuple(random.sample(range(-scope+1,scope), k=dim))
    return points


def optimalPointNaive(points: dict) -> str:
    """Naive solution for finding the optimal point that minimizes distance sum from all points"""
    minimalSum = float("inf")
    res = None

    for point, coordinates in points.items():
        distanceSum = 0
        for pt in points:
            distanceSquare = 0
            for i in range(len(coordinates)):
                distanceSquare += (coordinates[i] - points[pt][i])**2
            
            distanceSum += math.sqrt(distanceSquare)

        if distanceSum < minimalSum:
            minimalSum = distanceSum
            res = f"{point}: {coordinates}"   
    return res


def optimalPoint(points: dict) -> str:
    """Optimized solution for finding the optimal point that minimizes distance sum from all points"""
    ndarray = np.array([list(point) for point in points.values()])
    minimalSum = float("inf")
    optimalPoint = None

    for i in range(ndarray.shape[0]):
        distanceSum = sum(np.sqrt(np.sum((ndarray - ndarray[i])**2, axis=1)))

        if distanceSum < minimalSum:
            minimalSum = distanceSum
            optimalPoint = i+1

    return f"{optimalPoint}: {points[optimalPoint]}" 


def optimalPointEstimator(points: dict) -> str:
    """Using the centroid of points to estimate the optimal point"""
    centroid = sum(np.array([list(point) for point in points.values()]))/len(points)
    nearestDistance = float("inf")

    for point, coordinates in points.items():
        distance = sum((coordinates[i] - centroid[i])**2 for i in range(len(centroid)))
    
        if distance < nearestDistance:
            nearestDistance = distance
            res = f"{point}: {coordinates}" 
    return res