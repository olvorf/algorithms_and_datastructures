#Uses python3

import sys
import queue
from collections import deque


def distance(adj, s, t, n):
    dist = [float("inf")]*(n+1)
    dist[s] = 0
    queue = deque()
    queue.append(s)
    while queue:
        s_left = queue.popleft()
        for u in adj[s_left]:
            if dist[u] == float("inf"):
                queue.append(u)
                dist[u] = dist[s_left] + 1

    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n+1)]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    s, t = data[2 * m] , data[2 * m + 1] 
    distance = distance(adj, s, t, n)
    if distance == float("inf"):
        print(-1)
    else:
        print(distance)
