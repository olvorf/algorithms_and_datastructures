#Uses python3

import sys

def reach(adj, x, y, n):

    visited[x] = True

    for v in adj[x]:
        if visited[v] == False:
            reach(adj, v, y, n)
    if visited[y] == True:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n+1)]
    #x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n + 1)

    print(reach(adj, x, y, n))
