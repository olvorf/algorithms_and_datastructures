import sys
def knapsack(W, n, w):
    
    T =  [[0 for x in range(W+1)] for x in range(n+1)]
    
    for i in range(n+1):
        T[i][0] = 0
        for j in range(W+1):
            T[0][j] = 0
            T[i][j] = T[i-1][j]
            if w[i-1] <= j:
                val = T[i-1][j-w[i-1]] + w[i-1]
                if T[i][j] < val:
                    T[i][j] = val
    return T[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(knapsack(W,n,w))
            
    

