#Uses python3
'''
    author: kamran mostafavi
    This program determines an optimal way of exchanging money from one currency
    to all other currencies.

    given a directed graph with possibly negative edge weights, n vertices and
    m edges, starting vertix s, compute the shortest path s to all other vertices
    of the graph.

    input:
    n m      no.of.vertices no.of.directed_edges
    edge_1   from to weight (from some currency to some other currency, weight is -log_base_2 (exchange_rate)
    .
    edge_m
    s        start vertix (ie. starting currency)

    output
    for all vertices from 1 to n output the following on a separate line
    * if there is no path from s to u
    - if there is a path from s to u but there is no shortest path, else the length of the shortes path

    example:
    input:
    6 7
    1 2 10
    2 3 5
    1 3 100
    3 5 7
    5 4 10
    4 3 -18
    6 1 -1
    1    


    output:
    0
    10
    -      no shortest path
    -
    -
    *      not reacheable
'''
import sys

class bellman_ford():
    def explore(self, v, reachable, adj):
        '''
            explore graph starting at vertix v using the adjaceny list,
            mark vertix as visted if able to reach
        '''
        if reachable[v] == 1:
            return reachable
        reachable[v]=1
        for neighbor in adj[v]:
            reachable=self.explore(neighbor, reachable, adj)        
        return reachable       
    
    
    def bf_algo(self, adj, cost, s, dist, reachable, shortest, n, m):
        self.infinite=dist[0]
        #print (adj, cost, s, t, n)
        dist[s]=0           #distance of node from itself is 0
        #reachable=self.explore(s, reachable, adj)     #for some reason this does not give the correct results for test case 19
        prev = [-1 for _ in range(n)]
        for i in range (n+1):
            for u in range (n):
                for v in adj[u]:
                    #print (i,u,v)
                    cv=adj[u].index(v)
                    if dist[v] > dist[u] + cost[u][cv] and dist[u]!=self.infinite:
                    #if dist[v] > dist[u] + cost[u][cv]:
                        dist[v]=dist[u]+ cost[u][cv]
                        prev[v]=u
                        if i>=n-1:
                            shortest[v]=0
                    if shortest[u]==0:
                        shortest[v]=0
            #print (i, dist)
        #print("i:",i)
        #shortest contains nodes that are part of negative cycle
        #print ("prev: ",prev)
                     
        for v in range (n):             #for test case 19 to pass, reachability is determined if dist[v]!=infinite at the end of bf algo
            if dist[v]==self.infinite:
                reachable[v]=0
            else:
                reachable[v]=1
                       

def shortet_paths(adj, cost, s, dist, reachable, shortest, n, m):
    #write your code here
    #print (adj, cost, s, n, m)
    b=bellman_ford()
    b.bf_algo(adj,cost,s, dist, reachable, shortest,n,m)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest,n,m)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

