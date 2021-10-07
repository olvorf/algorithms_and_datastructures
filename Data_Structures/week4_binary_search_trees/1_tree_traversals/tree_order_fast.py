# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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
    #print(self.key[root], end=' ')
    result = result + self.inOrder(self.right[root])
    
    return result

  
  def preOrder(self, root):
    
    result = []

    if root == -1:
      return []
    
    
    result.append(self.key[root])
    #print(self.key[root], end=' ')
    result = result + self.preOrder(self.left[root])
    result = result + self.preOrder(self.right[root])
    
    return result
  
  
  def postOrder(self, root):
    
    result = []
    
    if root == -1:
      return []
    
    result = self.postOrder(self.left[root])
    result = result + self.postOrder(self.right[root])
    result.append(self.key[root])

      #self.inOrder(self.left[root])
      #self.inOrder(self.right[root])
      #print(self.key[root])
    
    return result

  

  

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder(0)))
	print(" ".join(str(x) for x in tree.preOrder(0)))
	print(" ".join(str(x) for x in tree.postOrder(0)))

threading.Thread(target=main).start()
