#Uses python3
'''
    author: Kamran Mostafavi
    This program computes the total minimum length of roads connecting n cities.
    (x,y) coordinate of cities are given as input. 

    input:
    n             no.of.cities
    x1 y1         (x,y) coordinate of city_1
    .
    xn yn         (x,y) coordinate of city_n
    
    output:
    total minium length of roads connecting cities - float with at least 7 dec places.

    use of prim algorithm to find the minimum length of roads.


    example:
    input:
    5
    0 0
    0 2
    1 1
    3 0
    3 2

    output:
    7.064495102
    
'''
import sys
import math
from heapq import *


def compute_distances(a,x,y):
    '''
        computes the distance between nodes a and all its neighbors
        input:
            node a    starting node number
            node b    ending node number
            x         x[] coordinates of all nodes
            y         y[] coordinates of all nodes
        output:
            d[]             distances between nodes a and all other nodes
     '''
    d=[]
    for i in range (len(x)):
        if i != a:
            m=x[a]-x[i]
            n=y[a]-y[i]
            d.append(math.sqrt(math.pow(m, 2)+math.pow(n, 2)))
    return d

def minimum_distance(x, y):
    '''
        x, y are arrays containing the coordinates x, y of input cities
    '''
    #print (x)
    #print (y)

    adj=[]      #build the adjancy list - This is a full mesh, where each node is neighbor of others
    for n in range (len(x)):
        adj.append([]) 
        for m in range (len(x)):
            if m==n:
                continue
            adj[n].append(m)       

    cost=[]     #cost is the weight of each edge connecting the nodes, it is a two dimensional array[v]=[distance of v to all other nodes in graph]
    for i in range (len (x)):
        cost.append (compute_distances(i,x,y))            

    #print (cost)
    #print (adj)

   
    #result = 0.
    #write your code here
    return sumDist(prim_algo(adj, cost, len(x)))  #use prim algo to return the min length of sum of all roads connecting the cities

def isInPQ(z,H):
    for i in range (len(H)):
        if z==H[i][1]:
            return True

    return False

def sumDist(dist):
    sum=0.0
    for i in range (len(dist)):
        sum=sum+dist[i]
    return sum
        

def prim_algo(adj, cost, n):
    infinity=10**19
    prev=[-1]*n
    dist=[infinity]*n

    s=0            #start with node 1 (can be any node)
    dist[s]=0      

    H=[]           #setup the priority Q
    for v in range(n):
        if v==s:
            heappush(H, [0,v])      #set priority to dist[v]
        else: 
            heappush(H, [infinity,v])
    #print ("H: ",H)

    while len(H) > 0:
        v=heappop(H)[1]                #extract min value
        #print ("extracting v:",v)
        #print ("H after extraction:",H)
        for z in adj[v]:
            #print ("v, z, adj_v:",v,z,adj[v])
            if isInPQ(z,H) and dist[z] > cost[v][adj[v].index(z)]:
                old=dist[z]
                dist[z]=cost[v][adj[v].index(z)]
                #print ("v, z, dist_z: ",v,z, dist[z])                
                prev[z]=v
                H[H.index([old,z])]=[dist[z],z]
                heapify(H)
                #print ("H: ",H)

    return (dist)

    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
