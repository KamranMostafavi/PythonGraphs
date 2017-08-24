#Uses python3
'''
    author: Kamran Mostafavi
    given a city with n intersections and m one way streets disminating from
    these intersections, determine if all intersections belong to a single SCC.
    ie: count = 1

    input:
        n m
        edge 1
        .
        edge m

    output:
        no.of.scc
   
'''
import sys

sys.setrecursionlimit(200000)
import sys
class graph:
    def __init__ (self, adj, adjR, n):
        self.adj=adj     #adjancy list for the graph
        self.adjR=adjR   #reversed adjancy list for the graph
        self.n=n
        self.visited=[0 for _ in range (n)]
        self.order=[]
        self.scc=[]
         
    def explore(self, v):
        '''
            explore graph starting at vertix v using the adjaceny list,
            mark vertix as visted if able to reach
            return linear order once done
            
        '''
        if self.visited[v]==1:
            return
        #print ("visiting: ",v)
        self.visited[v]=1
        for neighbor in self.adj[v]:
            self.explore(neighbor)
        #print ("leaving: ",v)
        self.order.append(v)      #postvisit_code: linear order vertix - find a sink and backtrace
        return             

    def exploreR(self, v):
        '''
            explore graph starting at vertix v using the reverse adjaceny list,
            mark vertix as visted if able to reach
            return linear order once done and 1 if strongly connected, 0 otherwise
            
        '''
        if self.visited[v]==1:
            return 0
        #print ("visiting: ",v)
        self.visited[v]=1
        for neighbor in self.adjR[v]:
            #print ("neighbor :", neighbor)
            self.exploreR(neighbor)
        #print ("leaving: ",v)
        self.order.append(v)      #postvisit_code: linear order vertix - find a sink and backtrace
        return 1            

def number_of_strongly_connected_components(adj,adjR,n):
    '''
        given a graph, return the number of strongly connected components in that graph.
        there is an excellent tutorial on youtube that goes into detail of SCC.
        https://www.youtube.com/watch?v=RpgcYiky7uw&t=936s

        1st explore the graph and create a topology sorted list in a form of a stack.
        2nd explore the reverse graph starting with vertix last pushed on the stack and
        keep count of SCC that are returned

    '''

    #1st explore the graph and create a topology sorted list in a form of a stack.

    result = 0
    #write your code here
    g=graph(adj, adjR, n)
    #print (g.adj)
    for vertix in range (n):
        g.explore(vertix)
    #print (g.order)

    order=g.order
    '''
        2nd explore the reverse graph starting with vertix last pushed on the stack and
        keep count of SCC that are returned
    '''
    g=graph(adj, adjR, n)
    #print (g.adjR)

    count = 0
    for _ in range (n):
        vertix=order.pop()
        #print ("poping: ",vertix)
        count = count + g.exploreR(vertix)

    #print (g.order)
    
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    #from adjacency list create reversed adjacency list to represent GR.
    adjR= [[] for _ in range(n)]
    for (b, a) in edges:
        adjR[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj, adjR,n))
