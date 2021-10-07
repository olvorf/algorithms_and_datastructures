def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def polyhash(string, prime, d ):
    hash = 0
    for i in range(len(string)-1,-1,-1):
        hash = (hash*d + ord(string[i])) % prime
    return hash

def precomputedhash(T, P, prime, d):
    t = len(T)
    p = len(P)
    s = T[t-p:]
    H = list([] for _ in range(t - p + 1))
    H[t-p] = polyhash(s, prime, d)
    y = 1
    for i in range(1,p+1):
        y = (y*d) % prime
    for i in range(t-p-1, -1, -1):
        H[i] = (d*H[i+1] + ord(T[i]) - y*ord(T[i + p])) % prime
    return H

def rabin_karp(T, P):
    t = len(T)
    p = len(P)
    prime = 1000000007
    d = 256
    result = []
    hash = polyhash(P, prime, d)
    H = precomputedhash(T, P, prime, d)
    for i in range(t-p + 1):
        if hash == H[i]:
            result.append(i)
    return result

if __name__ == '__main__':
    #print_occurrences(rabin_karp(*read_input()))
    P = input()
    T = input()
    results = rabin_karp(T, P)
    for res in results:
        print(res, end=' ')



