def fibonacci_fast(n):
    prev = 1
    curr = 0
    for i in range(n):
        next = curr + prev
        prev = curr
        curr = next
    return curr % 10

n = int(input())
print(fibonacci_fast(n))