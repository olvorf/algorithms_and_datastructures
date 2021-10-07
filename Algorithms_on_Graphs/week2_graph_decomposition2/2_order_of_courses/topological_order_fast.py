#Uses python3

import sys

def reach(adj, x, visited, stack):

    visited[x] = True
    #stack = []
    for v in adj[x]:
        if visited[v] == False:
            reach(adj, v, visited, stack)
    stack.append(x)



def toposort(adj):
    visited = [False] * len(adj)
    stack = []
    for i in range(len(adj)):
        if visited[i] == False:
            reach(adj, i, visited, stack)
    return stack

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n+1)]
    for (a, b) in edges:
        adj[a].append(b)
    order = toposort(adj)
    order.reverse()

    for x in order[:-1]:
        print(x, end=' ')

