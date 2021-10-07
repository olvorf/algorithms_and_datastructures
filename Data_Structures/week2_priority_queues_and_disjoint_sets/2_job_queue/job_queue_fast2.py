# python3

def max_heapfy(a,i):
    m = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < len(a):
        if a[l][0] < a[m][0]:
            m = l
        elif a[l][0] == a[m][0]:
            if a[l][1] < a[m][1]:
                m = l
    
    if r < len(a):
        if a[r][0] < a[m][0]:
            m = r
        elif a[r][0] == a[m][0]:
            if a[r][1] < a[m][1]:
                m = r
    if i != m:
        a[i], a[m] = a[m], a[i]
        max_heapfy(a, m)

        


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    assigned_workers = [None]*len(jobs)
    start_times = [None]*len(jobs)
    next_free_time = [(0, i) for i in range(n_workers)]
    for i in range(len(jobs)):
        assigned_workers[i] = next_free_time[0][1]
        start_times[i] = next_free_time[0][0]
        next_free_time[0] = (next_free_time[0][0] + jobs[i], next_free_time[0][1])
        max_heapfy(next_free_time,0)
    return assigned_workers, start_times



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_workers, start_times = assign_jobs(n_workers, jobs)

      

    for i in range(len(jobs)):
          print(assigned_workers[i], start_times[i])   

    
if __name__ == "__main__":
    main()
