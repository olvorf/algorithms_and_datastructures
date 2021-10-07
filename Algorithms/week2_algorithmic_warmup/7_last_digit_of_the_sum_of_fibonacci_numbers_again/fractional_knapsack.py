# Uses python3
import sys
def get_optimal_value(capacity, weight, value ):
    
    index = list(range(len(value)))
    n = len(weight)
    cost=[0]*n
    for i in range(n):
        cost[i] = value[i]//weight[i]
    
    index.sort(key=lambda i: cost[i], reverse=True)

    total = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i]  = 1
            capacity = capacity - weight[i]
            total = total + value[i]
        else:
            fractions[i] = capacity/weight[i]
            total = total + value[i]*capacity/weight[i]
            break
    return total

 


if __name__ == "__main__":
    
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, capacity = data[0:2]
    value = data[2:(2 * n + 2):2]
    weight = data[3:(2 * n + 2):2]
    #weight = [10, 40, 20, 30]
    #value = [60, 40, 100, 120]
    #capacity = 50
    opt_value = get_optimal_value(capacity, weight, value)
    print("{:.10f}".format(opt_value))
