import sys
import math
def binary_search(A, x):
    left = 0
    right = len(A)-1
    while left <= right:
        m = math.floor((left+right)/2)
        if A[m] < x:
            left = m+1
        elif A[m] > x:
            right = m-1
        else:
            return m
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
