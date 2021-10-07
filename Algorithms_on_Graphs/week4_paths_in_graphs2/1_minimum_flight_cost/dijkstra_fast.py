#Uses python3

import sys
import queue


def dijkstra(adj, nodes, edges, source):
    Q = []
    distance = [float("inf")]*(n+1)
    distance[source] = 0

    temp = 
            


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n+1)]
    cost = [[] for _ in range(n+1)]
    for ((a, b), w) in edges:
        adj[a].append(b )
        cost[a].append(w)
    s, t = data[0] , data[1] 
    print(dijkstra(adj, cost, s, t))
