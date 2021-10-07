#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__stack2 = []

    def Push(self, a):
        self.__stack.append(a)
        if (len(self.__stack) == 1):
            self.__stack2.append(a) 
            return

        if (a > self.__stack2[-1]): 
            self.__stack2.append(a) 
        else:
            self.__stack2.append(self.__stack2[-1])

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        assert len(self.__stack2)
        self.__stack2.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__stack2[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
