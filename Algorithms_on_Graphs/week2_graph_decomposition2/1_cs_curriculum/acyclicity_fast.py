#Uses python3

import sys

def explore(adj, x, color):
    color[x] = "Grey"

    for vertex in adj[x]:
        
        
        if color[vertex] == "Grey":
            return True
        
        elif color[vertex] == "White" and explore(adj, vertex , color) == True:
            return True

    color[x] = "Black"   
    return False
    
    #color[x] = "Black"
    #return False    
       # if color[vertex] == "White" and explore(adj, vertex , color) == True:
        #    return True
        #color[x] = "Black"
    #return False



    
        


def is_cycle(adj):
    color = ["White"] * (n+1) 

    for i in range(n+1):
        if color[i] == "White":
            if explore(adj, i, color) == True:
                
                return 1
    return 0


    



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #x, y = data[2 * m:]
    adj = [[] for _ in range(n+1)]
    #x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a].append(b)
        #adj[b].append(a)
    #visited = [False] * (n + 1)

    print(is_cycle(adj))

    #print("Graph contains cycle" if is_cycle(adj) == True\
    #    else "Graph doesn't contain cycle" )
