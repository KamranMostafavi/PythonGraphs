#Uses python3
import sys
import math

class disjointSet:
    def __init__(self, size):
        self.size=size
        self.rank=[0]*size
        self.parent= list(range(0,size))
                          
    def Find(self,i):
        while i != self.parent[i]:
            i= self.parent[i]
        return i

    def betterFind(self, i):
        #This does path compression which in effect reduces the height of the set (which is a tree)
        if i != self.parent[i]:
            self.parent[i] = self.betterFind(self.parent[i])
        return self.parent[i]
                          
    def Union(self,j,i):
        #This union puts a set with samller rank under the other set. If the ranks of the two sets are equal then the rank of the resulting set is one greater.
        i_id=self.betterFind(i)
        j_id=self.betterFind(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id]=i_id #merge set with lower depth to set with higher depth
        else:
            self.parent[i_id]=j_id
            if self.rank [i_id]== self.rank[j_id]:    
                self.rank[j_id]=self.rank[j_id]+1  #increment rank of the set id if the two sets were of equal depth
                
    def countSets(self):
        s=[]
        for e in self.parent:
            if e not in s:
                s.append(e)
        return len(s)

def edgeIn(edge,arr):
    for i in range (len(arr)):
        if edge==arr[i][1]:
            return True
    return False

def compute_edge_distances(x,y):
    '''
        computes the distance between nodes a and all its neighbors
        input:
            x         x[] coordinates of all nodes
            y         y[] coordinates of all nodes
        output:
            d[]       [[d,[u,v]]  starting node, ending node, distance    
     '''
    d=[]
    for i in range (len(x)):
        for j in range (len(x)):
            #if i != j and not edgeIn([j,i],d):
            if i != j:
                m=x[j]-x[i]
                n=y[j]-y[i]
                d.append([math.sqrt(math.pow(m, 2)+math.pow(n, 2)),[i,j]])
    #print ("cost: ", d)
    d.sort()
    return d

def sumDist(dist):
    sum=0.0
    for i in range (len(dist)):
        sum=sum+dist[i][0]
    return sum



def kruskal_algo(cost, n,k):
    '''
    Given a graph defined by adjancy list and edge weights, implement Kruskal
    algorithm and return the minimum edge weight between number of clusters/sets
    passed in k.
    
    '''
    myset=disjointSet(n)    #initializes each node to be in unique set
    X=[]                    #initializes set of edges

  
    for c,[u,v] in cost:
        if myset.betterFind(u)!= myset.betterFind(v):
            if n-len(X)==k:   #no.of.clusters= no.of.nodes-no.of.edges
                return c
            X.append([c,[u,v]])
            myset.Union(u,v)

   
def clustering(x, y, k):
    
    #cost is the weight of each edge connecting the nodes, it is a two dimensional array[v]=[distance of v to all other nodes in graph]
    cost=compute_edge_distances(x,y)
        
    
    #write your code here

    return kruskal_algo(cost, len(x),k) 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
