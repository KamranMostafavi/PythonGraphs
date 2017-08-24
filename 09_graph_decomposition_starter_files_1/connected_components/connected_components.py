#Uses python3
'''
    author: Kamran Mostafavi
    This program determines the number of connected components in an undirected graph.

    Input:
    n m    ;n=no.of.vertices m=no.of.edges
    edge 1
    .
    edge m

    Output:
    print no.of.connected_components
    
'''

import sys
class graph:
    def __init__ (self, adj, n):
        self.adj=adj
        self.n=n
        self.visited=[0 for _ in range (n)]
        
    def explore(self, v):
        '''
            explore graph starting at vertix v using the adjaceny list,
            mark vertix as visted if able to reach
        '''
        if self.visited[v] == 1:
            return True
        self.visited[v]=1
        for neighbor in adj[v]:
            self.explore(neighbor)        
        return False       

def number_of_components(adj,n):
    '''
        determine no of connected components in a graph given an adjancy list
        input:
            adj = vertix adjancy list (ex:[[1, 3], [0, 2], [1, 3], [2, 0]])

        output:
            count = count of connected components
    '''

    g = graph(adj,n)

    count = 0      #each time a connected component is discovered the count is incremented
    for vertix in range (n):
        if g.explore(vertix): #returns true if vertix was visited
            continue          #goto next vertix if this one was visited
        count += 1            #here when completed visiting the connected components for vertix, increment cc count

    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]    #n = no.of.vertices m=no.of.edges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2])) # 
    adj = [[] for _ in range(n)]    
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj,n))
