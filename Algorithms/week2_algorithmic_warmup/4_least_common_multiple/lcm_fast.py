
def gcd_fast(a,b):
    while b!=0:
        t = b
        b = a % b
        a = t
    return a


def lcm_fast(a,b):
    lcm = a / gcd * b
    return int(lcm)
    
if __name__ == '__main__':
    a, b = map(int, input().split())
    gcd  = gcd_fast(a,b)
    print(lcm_fast(a, b))

