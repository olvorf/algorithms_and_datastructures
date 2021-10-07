import sys

def get_majority_element(a, left, right):
    
    a.sort()
    count = 1
    max_element = -1
    temp = a[0]
    f = 0
    
    for i in range(1,len(a)):
        if(temp == a[i]):
            count = count + 1
        else:
            count = 1
            temp = a[i]
        if max_element < count :
            max_element = count
            
            if(max_element > (len(a)//2)):
                f = 1
                break 
    if f == 1:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, len(a)))
     