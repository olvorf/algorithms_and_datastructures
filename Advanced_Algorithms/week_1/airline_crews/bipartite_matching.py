# python3

def make_network(n, m, bip):
    graph = [[0] * (n + m + 2) for _ in range(n + m + 2)]
    for i in range(1, n + 1):
        graph[0][i] = 1
        for j in range(m):
            graph[i][n + 1 + j] = bip[i - 1][j]
    for k in range(n + 1, n + m + 1):
        graph[k][-1] = 1
    return graph

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

def ford_fulkerson(graph, s, t, n_flights):
    n = len(graph)
    parent = [0] * n
    max_flow = 0

    while bfs(graph, s, t, parent):
        path_flow = float('inf')
        start  = t
        while(start != s):
            path_flow = min(path_flow, graph[parent[start]][start])
            start = parent[start]
        

        v = t
        while(v != s):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
        
        #max_flow += path_flow

        
    matches = [-1] * n_flights
    for i in range(n):
        if graph[n-1][i] == 1:
                person = i - n_flights
                flight = graph[i].index(1)
                matches[flight -1] = person
    return matches
    
    #return max_flow


if __name__ == '__main__':
    n_flights, n_crew = map(int, input().split())
    bipartite = [list(map(int, input().split())) for i in range(n_flights)]

    residual_graph = make_network(n_flights, n_crew, bipartite)
    t = n_flights + n_crew + 1
    s  = 0
    matching = ford_fulkerson(residual_graph, s, t, n_flights)
    for e in matching:
        print(e, end=' ')

