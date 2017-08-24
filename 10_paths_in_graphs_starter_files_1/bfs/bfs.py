#Uses python3

import sys
import queue

'''
    author: Kamran Mostafavi
    This is an implementation of breadth first search. The search starts at s and computes the
    distance of all nodes to S. it then returns the distance for node t to s or -1 if t can not
    be reached from s.
    I have also added code necessary to compute the nodes along the shortest path eventhough that
    is not required.
    
'''

class bfs:
    def breathFirstSearch(self, adj, n, s, t):
        dist = [-1 for _ in range(n)] #init distance to infinity for all vertices
        dist[s]=0
        prev = [-1 for _ in range(n)]       
        q=[]
        q.append(s)
        while len(q) > 0:
            u=q[0]
            q.remove(q[0])
            for v in adj[u]:
                if dist[v] == -1:
                    q.append(v)
                    dist[v]=dist[u]+1
                    prev[v]=u
        return dist[t]

def distance(adj, s, t, n):
    #write your code here
    '''
        given a undirected graph and two vertices s and t, determine the shortest
        path between the two vertices. If they are not connected (ie: no paths between
        them, return -1
        example of input: 
        4 4         no.of.nodes no.of.edges
        1 2         edge 1
        4 1         .
        2 3         .
        3 1         edge 4
        2 4         start.node  end.node

        Output:
        2
    
    '''
    g=bfs()
    return g.breathFirstSearch(adj,n,s,t)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]  #build adjancy list which is the list of neighbors
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1  #s, t are the start and end nodes for which distance is computed
    print(distance(adj, s, t, n))
