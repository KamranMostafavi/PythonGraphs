#Uses python3
'''
    author: Kamran Mostafavi
    this program computes the least cost for traveling from one city to some
    destination. Dijkstra Algorithm is use to compute the minimum cost

    input:
    n m    no.of.cities no.of.routes
    route 1   start_city end_city cost
    .
    route m
    x y    start_city end_city

    output:
    z      min_cost_of_traveling_from_x_to_y
           -1 if there is no route between x and y


Example:

    5 9
    1 2 4
    1 3 2
    2 3 2
    3 2 1
    2 4 2
    3 5 4
    5 4 1
    2 5 3
    3 4 4
    1 5

output:
    6
'''
import sys
from heapq import *

class dijkstra:
    infinite=1000000000
    def dks(self, adj, cost, s, t, n):
        #print (adj, cost, s, t, n)
        dist = [ self.infinite for _ in range(n)] #init distance to infinity for all vertices
        dist[s]=0
        prev = [-1 for _ in range(n)]       
        H=[]
        for v in range(n):
            if v==s:
                heappush(H, [0,v])      #set priority to dist[v]
            else: 
                heappush(H, [self.infinite,v])

        while len(H) > 0:
            u=heappop(H)[1]                #extract min value
            for v in adj[u]:
                if dist[v] > dist[u] + cost[u][adj[u].index(v)]:
                    #print (H)
                    old=dist[v]
                    dist[v]=dist[u]+ cost[u][adj[u].index(v)]
                    prev[v]=u
                    H[H.index([old,v])]=[dist[v],v]
                    heapify(H)
        return dist[t]

def distance(adj, cost, s, t, n):
    #write your code here
    d=dijkstra()
    out=d.dks(adj, cost, s, t, n)
    if out==d.infinite:
        return -1
    else:
        return out

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t, n))
