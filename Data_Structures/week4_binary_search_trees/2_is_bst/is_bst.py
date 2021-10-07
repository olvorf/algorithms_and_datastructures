#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
def inOrder(tree):
    root = 0
    result = []
    
    if root == -1:
      return []
    

    result = inOrder(left[root])
    result.append(self.key[root])
    #print(self.key[root], end=' ')
    result = result + self.inOrder(self.right[root])
    
    return result
def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
