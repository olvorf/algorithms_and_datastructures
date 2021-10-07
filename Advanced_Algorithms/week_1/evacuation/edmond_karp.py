# python3


def bfs(graph, s, t, parent):
    n = len(graph)
    visited = [False] * n

    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for index, value in enumerate(graph[u]):
            if visited[index] == False and value > 0:
                queue.append(index)
                visited[index] = True
                parent[index] = u
                if index == t:
                    return True
    return False

def ford_fulkerson(graph, s, t):
    n = len(graph)
    parent = [-1] * n
    max_flow = 0

    while bfs(graph, s, t, parent):
        path_flow = float('inf')
        start  = t
        while(start != s):
            path_flow = min(path_flow, graph[parent[start]][start])
            start = parent[start]
        
        max_flow += path_flow

        v = t
        while(v != s):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    
    return max_flow


if __name__ == '__main__':
    n_city, n_edges = map(int, input().split())
    t = n_city-1
    s  = 0
    residual_graph = [[0] * n_city for i in range(n_city)]
    for _ in range(n_edges):
        u, v, capacity = map(int, input().split())
        residual_graph[u - 1][v - 1] += capacity
    #print(residual_graph)
    max_flow = ford_fulkerson(residual_graph, s, t)
    print(max_flow)

