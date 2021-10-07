import math
def Find(x, parent):
    if x != parent[x]:
        parent[x] = Find(parent[x], parent)
    return parent[x]

def Union(x,y, parent, rank):
    x_parent = Find(x, parent)
    y_parent = Find(y, parent)

    if rank[x_parent] < rank[y_parent]:
        parent[x_parent] = y_parent
    elif rank[x_parent] > rank[y_parent]:
        parent[y_parent] = x_parent
    else:
        parent[y_parent] = x_parent
        rank[x_parent] += 1

def kruskal(edges, n):
    dist = 0
    edges.sort(key=lambda i: i[2]) 
    parent = [i for i in range(n)]
    rank = [0] * n

    for a, b, w in edges:
        if Find(a, parent) != Find(b, parent):
            dist += w
            Union(a,b, parent, rank)
    return dist

if __name__ == '__main__':
    n = int(input())
    points = [None] * n # 0-based index
    for i in range(n):
        a, b = map(int, input().split())
        points[i] = (a, b)
    edges = [] # (start, end, weight)

    for i in range(n):
        (x0, y0) = points[i]
        for j in range(i + 1, n):
            (x, y) = points[j]
            distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
            edges.append((i, j, distance))
    min_length = kruskal(edges, n)
    print("{0: .9f}".format(min_length))

    

