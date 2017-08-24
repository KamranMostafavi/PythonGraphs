#Uses python3
'''
    author: Kamran Mostafavi
    given n courses and m directed edges between them representing pre-requisites
    create a linearly ordered list of courses (topological order)
    it is given that the graph of the courses is a DAG.

    input:
        n m
        edge 1
        .
        .
        edge m
    output:
        linearly ordered list of n courses
            
'''

import sys
class graph:
    def __init__ (self, adj, n):
        self.adj=adj
        self.n=n
        self.visited=[0 for _ in range (n)]
        self.order=[]
         
    def explore(self, v):
        '''
            explore graph starting at vertix v using the adjaceny list,
            mark vertix as visted if able to reach
            return linear order once done
            
        '''
        if self.visited[v]==1:
            return
        
        self.visited[v]=1
        for neighbor in adj[v]:
            self.explore(neighbor)
        self.order.insert(0,v)      #linear order vertix - find a sink and backtrace
        return             


def toposort(adj, n):
    g=graph(adj,n)
    for vertix in range (n):
        g.explore(vertix)
    return g.order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj,n)
    for x in order:
        print(x + 1, end=' ')

