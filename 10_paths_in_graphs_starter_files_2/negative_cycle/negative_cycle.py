#Uses python3
'''
    author: Kamran Mostafavi
    this program detects a negative cycle in a weighted graph using bellman-ford
    agorithm

    input:
    n m      no.of.vertices no.of.edges
    edge 1   form to weight
    .
    .
    edge m


    output:
        print 1 if a negative cycle is in the graph, 0 otherwise

    example:
    input:
    4 4
    1 2 -5
    4 1 2
    2 3 2
    3 1 1

    output:
    1
'''

import sys


class bellman_ford():
    infinite=1000000000
    def bf_algo(self, adj, cost, s, n, m):
        #print (adj, cost, s, t, n)
        dist = [ self.infinite for _ in range(n)] #init distance to infinity for all vertices
        dist[s]=0
        prev = [-1 for _ in range(n)]       
        for i in range (n-1):
            for u in range (n):
                for v in adj[u]:
                    #print (i,u,v)
                    if dist[v] > dist[u] + cost[u][adj[u].index(v)]:
                        dist[v]=dist[u]+ cost[u][adj[u].index(v)]
                        prev[v]=u
            #print (i, dist)
        for u in range (n):
            for v in adj[u]:
                if dist[v] > dist[u] + cost[u][adj[u].index(v)]:
                    return 1        
        return 0

def negative_cycle(adj, cost, n, m):
    #write your code here
    b=bellman_ford()
    return (b.bf_algo(adj,cost,0,n,m))

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
    print(negative_cycle(adj, cost, n, m))
