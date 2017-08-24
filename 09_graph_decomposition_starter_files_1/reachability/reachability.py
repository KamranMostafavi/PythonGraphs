#Uses python3

import sys
'''
    author: Kamran Mostafavi
    This code determines if two nodes in an undirected graph are connected
    input:
    n m     ;no of vertices, number of edges
    edge 1
    .
    edge m
    x y     ;start vertix, end vertix

    output:
    prints 1 if x and y are connected, otherwise prints 0
'''

class graph:
    def __init__ (self, adj, n, x, y):
        self.adj=adj  #adjacency list (list of neighbors)
        self.n=n      #no.of.vertices
        self.x=x      #start vertix
        self.y=y      #end vertix
        self.visited=[0 for _ in range (n)] #visited array for vertices
        
    def explore(self, v):
        '''
            explore graph starting at vertix v using the adjaceny list,
            mark vertix as visted if able to reach
        '''
        if self.visited[v] == 1:
            return
        self.visited[v]=1
        for neighbor in adj[v]:
            self.explore(neighbor)        
        return        

def reach(adj, n, x, y):
    '''
        determine if given an adjacency list for a graph, there is a path between vertix x and y.
        input:
            adj = vertix adjancy list (ex:[[1, 3], [0, 2], [1, 3], [2, 0]])
            n = number of vertices in the graph
            x = start vertix
            y = end vertix
        output:
            0 = No path found
            1 = path found connecting x and y vertices
    '''
    #write your code here
    g=graph(adj,n,x,y)
    #print (g.visited)
    g.explore(x)    #start exploring with start vertix
    #print (g.visited)
    return g.visited[y] #if x and y are connected then y must have been visited

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split())) #convers string of integers to a list 
    #print (data)
    n, m = data[0:2]    #n has no.of.vertices, m has no.of.edges
    data = data[2:]     
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2])) #extract the edges and create a list of it
    #print (edges)
    x, y = data[2 * m:] #x,y indicate start vertix and end vertix
    #print (x,y)
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1 #convert vertix numbers to 0 based as stored in arrays - coverts vertix 1 to node 0 with key 1 as its value
    for (a, b) in edges: #build adjancy list (ie: list of neighbors)
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print (adj)
    print(reach(adj, n, x, y))
