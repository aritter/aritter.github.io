import numpy as np
import matplotlib.pyplot as plt
import sys
import math

N = 100

def DistancesBetweenRandomPoints(D):
    data = np.random.random((N,D))

    dsum = 0.0
    dlist = []
    for i in range(N):
        for j in range(N):
            if i != j:
                dlist += [np.linalg.norm(data[i,:] - data[j,:])]       #Euclidean distance between rows i and j
                count += 1
    return dlist
            
plt.hist([(x / math.sqrt(2)) for x in DistancesBetweenRandomPoints(2)])
plt.hist([(x / math.sqrt(10)) for x in DistancesBetweenRandomPoints(10)])
plt.hist([(x / math.sqrt(100)) for x in DistancesBetweenRandomPoints(100)])
plt.hist([(x / math.sqrt(1000)) for x in DistancesBetweenRandomPoints(1000)])
plt.hist([(x / math.sqrt(10000)) for x in DistancesBetweenRandomPoints(10000)])
plt.show()
