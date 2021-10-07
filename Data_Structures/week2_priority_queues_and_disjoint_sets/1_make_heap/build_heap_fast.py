# python3
import math 
swaps = []
def min_heap(data, n, i):
    smallest = i
    left = 2*i+1
    right = 2*i+2

    # If left child is larger than root
    if left < n and data[left] < data[smallest]:
        smallest = left
  
    # If right child is larger than largest so far
    if right < n and data[right] < data[smallest]:
        smallest = right
  
    # If largest is not root
    if smallest != i:
        swaps.append((i, smallest))
        data[i], data[smallest] = data[smallest], data[i]
  
        # Recursively heapify the affected sub-tree
        min_heap(data, n, smallest)
    return swaps
    


def build_heap(data, n):
    heap_size = len(data)
    for i in range(math.floor(heap_size/2), -1, -1):
      swaps =   min_heap(data, n, i)
    return swaps

#def printHeap(data, n):
#    print("Array representation of Heap is:");
#  
#    for i in range(n):
#        print(data[i], end = " ");
#    print();


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    #build_heap(data, n);
    #printHeap(swap, n);
    

    swaps = build_heap(data,n)
    

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
