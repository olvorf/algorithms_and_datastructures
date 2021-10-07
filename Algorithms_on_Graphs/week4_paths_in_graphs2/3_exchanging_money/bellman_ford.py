
from collections import deque
import sys

def bellman_ford(adj, edges, n,source):
    dist = [float('inf')] * (n+1)
    dist[source] = 0
    prev = [None]*(n+1)
    negative_nodes = deque()
    for i in range(n):
        for a,b,w in edges:
            if  dist[b] > dist[a] + w:
                dist[b] = dist[a] + w
                prev[b] = a
                if i == n - 1:
                    negative_nodes.append(b)

    visited = [False]*(n+1)
    while negative_nodes:
        v_left = negative_nodes.popleft()
        visited[v_left] = True
        dist[v_left] = '-'
        for v in adj[v_left]:
            if not visited[v]:
                negative_nodes.append(v)
    return dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(3 * m):3], data[1:(3 * m):3], data[2:(3 * m):3]))
    #data = data[3 * m:]
    adj = [[] for _ in range(n+1)]
    #cost = [[] for _ in range(n)]
    for (a, b, w) in edges:
        adj[a].append(b)
    #    cost[a - 1].append(w)
    s = data[-1]
    #s -= 1
    #distance = [10**19] * n
    #reachable = [0] * n
    #shortest = [1] * n
    distance = bellman_ford(adj, edges,n, s)
    for dist in distance[1:]:
        if dist == float('inf'):
            print('*')
        else:
            print(dist)