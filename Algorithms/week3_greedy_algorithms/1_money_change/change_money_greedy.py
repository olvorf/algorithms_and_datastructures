# Uses python3
import sys

def get_change(m):

    deno = [10, 5, 1]
    n=len(deno)
    ans=[]
    
    for i in range(n):
        while(m >= deno[i]):
            m = m-deno[i]
            ans.append(deno[i])
        i = i + 1 
    return len(ans)

if __name__ == '__main__':
    m = int(input())
    #m = int(sys.stdin.read())
    print(get_change(m))
