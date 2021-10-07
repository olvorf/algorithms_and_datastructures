# Uses python3
import sys
import random

def partition3(A, l, r):
    less = l  # We initiate lss to be the part that is less than the pivot
    mid = less   # We scan the array from left to right
    greater = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while mid <= greater:      # Starting from the first element.
        if A[mid] < pivot:
            temp = A[mid]
            A[mid] = A[less]
            A[less] = temp 
            less =less + 1
            mid = mid + 1
        elif A[mid] > pivot:
            temp = A[mid]
            A[mid] = A[greater]
            A[greater] = temp
            greater = greater - 1
        else:
            mid = mid + 1
            
    return less, greater
    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    less, greater = partition3(a, l, r)
    randomized_quick_sort(a, l, less - 1);
    randomized_quick_sort(a, greater + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
