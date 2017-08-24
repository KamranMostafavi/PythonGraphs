#Uses python3
'''
    author:Kamran Mostafavi
    Here a directed graph of n vertices and m edges are given and this program
    will determine if there is a cycle in it.

    input
    n m
    edge 1
    .
    edge m

    output
    print 1 if a cycle is detected otherwise print 0
'''
import sys

class graph:
    def __init__ (self, adj, n):
        self.adj=adj
        self.n=n
        self.visited=[0 for _ in range (n)]
        self.cycle=False
        self.start=-1
        
    def explore(self, v):
        '''
            explore graph starting at vertix v using the adjaceny list,
            mark vertix as visted if able to reach
        '''
        if self.visited[v] == 1 and self.start==v:
            self.cycle=True
            #print ("cycle detected: ",v)
            return True         #if cycling back to vertix
        elif self.visited[v] == 1:
            return True
        
        self.visited[v]=1
        #print ("visited: ",v)
        for neighbor in adj[v]:
            self.explore(neighbor)        
        return False            #if no cycle to this veritx


def acyclic(adj, n):
    '''
        determine if graph is acyclic (ie: no cycles detected)
        output:
            0 if no cycles detected
            1 if cycles are detected
    '''
    g=graph(adj, n)
    #print (g.adj)
    
    for vertix in range (n):
        # clear visited flags before exploring
        g.visited=[0 for _ in range (n)]
        g.cycle=False
        g.start=vertix
        #print ("start with: ",vertix)
        g.explore(vertix)
        if g.cycle==True:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
