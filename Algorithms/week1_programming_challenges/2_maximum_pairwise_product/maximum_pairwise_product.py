def maximum_pairwise_product(A):
    index_1 = 1
    n = len(A)
    for i in range(2,n):
        if A[i] > A[index_1]:
            index_1 = i
    A[n-1], A[index_1] = A[index_1], A[n-1]

    index_1 = 1
    for i in range(2,n-1):
        if A[i] > A[index_1]:
            index_1 = i
    A[n-2], A[index_1] = A[index_1] , A[n-2]
    return A[n-1]*A[n-2]



if __name__=='__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(maximum_pairwise_product(input_numbers))