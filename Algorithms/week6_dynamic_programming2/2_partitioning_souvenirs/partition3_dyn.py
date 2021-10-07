import sys

def partition3(arr):
    sum = 0
    i, j = 0, 0
    
    n = len(arr)
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 3 != 0:
        return 0
 
    part = [[1 for i in range(n + 1)]
            for j in range(sum // 3 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = 1
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 3 + 1):
        part[i][0] = 0
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 3 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or
                              part[i - arr[j - 1]][j - 1])
 
    return part[sum // 3][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
