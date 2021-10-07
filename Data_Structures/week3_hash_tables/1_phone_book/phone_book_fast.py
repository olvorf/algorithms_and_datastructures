book = [None]*10000000

def add(number, name):
    book[number] = name

def delete(number):
    if book[number] is not None:
        book[number] = None

def find(number):
    if book[number] is None:
        return "not found"
    return book[number]

def process_queries(queries):
    for query in queries:
        q  = query.split()
        input = q[0]
        number = int(q[1])
        if input == "add":
            add(number, q[2])
        elif input == "del":
            delete(number)
        elif  input == "find":
            print(find(number))


if __name__ == "__main__":
    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries) 
