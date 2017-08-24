#Uses python3
'''
    author: kamran mostafavi
    This program determines if the input graph is bipartite. In a bipartite graph, the end points of each edge has nodes that are different say
    one node is black and the next node is white. In mathematical terms if two nodes that are in the same level (i.e: distance from origin) are
    connected, then the graph is not bipartite.
'''
import sys
import queue
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
                elif dist[v]==dist[u]:  #check to see if not bipartite (u and v are nodes that are connected and at same level
                    return 0
        return 1

def bipartite(adj,n):
    '''
        determine if the graph is bipartite - that is if two nodes in the same level/distance are connected the graph is not bipartite, otherwise it is.
        return 0 if not, 1 if bipartite
    '''
    g=bfs()
    return g.breathFirstSearch(adj,n,0,n-1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj,n))
