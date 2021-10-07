
def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def rabin_karp(P,T):
    d = 256
    q = 1000000007
    n = len(T)
    m = len(P)
    h = pow(d,m-1,q)
    p = 0 #hash value for pattern   
    t = 0 #hash value for text
    output = []
    for i in range(m):
        p = (d*p + ord(P[i])) % q
        t = (d*t + ord(T[i])) % q 
    for i in range(n-m + 1):
        if p == t:
            match = True
            for j in range(m):
                if P[j] != T[i+j]:
                    match = False
                    break
            if match:
                output = output + [i]
        
        if i < n-m:
            #t = (d*(t - ord(T[i])*h) + ord(T[i+m])) % q
            t = (t - ord(T[i])*h) % q
            t = (d*t + ord(T[i+m])) % q
            t = (t + q) % q
    return output
if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))



