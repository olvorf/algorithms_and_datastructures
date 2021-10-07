import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, root):
        result = []
    
        if root == -1:
            return []
    
        result = self.inOrder(self.left[root])
        result.append(self.key[root])
        result = result + self.inOrder(self.right[root])
    
        return result

    def isBST(self, tree):
        nodes = self.inOrder(tree)
        for i in range(1,len(nodes)):
            if nodes[i] <= nodes[i-1]:
              return False
        return True

def main():
    tree = TreeOrders()
    tree.read()
    n = tree.n
    #print(" ".join(str(x) for x in tree.inOrder(0)))
    if n == 0 or tree.isBST(0):
        print('CORRECT')
    else:
        print('INCORRECT')
threading.Thread(target=main).start()
