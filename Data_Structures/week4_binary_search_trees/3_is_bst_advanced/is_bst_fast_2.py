import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c


def isBST(tree):
    stack = [(float('-inf'), tree[0], float('inf'))]
    while stack:
        min, root, max = stack.pop()
        if root.key < min or root.key >= max:
            return False
        if root.left != -1:
            stack.append((min, tree[root.left], root.key))
        if root.right != -1:
            stack.append((root.key, tree[root.right], max))
    return True


def main():
    n = int(input())
    nodes = [0 for _ in range(n)]
    for i in range(n):
        a, b, c = map(int, input().split())
        node = Node(a, b, c)
        nodes[i] = node
    if n == 0 or isBST(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()