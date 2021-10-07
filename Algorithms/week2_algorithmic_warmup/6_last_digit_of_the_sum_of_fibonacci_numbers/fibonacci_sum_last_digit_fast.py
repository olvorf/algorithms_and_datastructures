
def fib(n):
    n = int(n)
    f = [0]*(n+1)

    if (n == 0):
        return 0
    if (n == 1 or n == 2):
        return (1) 
    if (f[n] == True):
        return f[n] 

    k = (n+1)/2 if (n & 1) else n/2

    f[n] = (fib(k) * fib(k) + fib(k-1) * fib(k-1)) if (n & 1) else (2 * fib(k-1) + fib(k)) * fib(k)
    return f[n] 

def calculateSum(n):

    return (fib(n+2) - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(calculateSum(n)) 
