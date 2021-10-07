# python3
import sys

def sort_characters(text):
  n = len(text)
  order = [0]*n
  count = [0]*27
  for char in text:
      count[char] += 1
  for i in range(n-1):
    count[text[i]] = count[text[i]] + 1
  for j in range(1,26):
    count[j] = count[j] + count[j-1]
  for i in range(n-1,-1,-1):
    c = text[i]
    count[c] = count[c] - 1
    order[count[c]] = i
  return order

def SortCharacters(s):
    order = [0] * len(s)
    count = {'$': 0, "A": 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        count[char] += 1
    ele = ['$', 'A', 'C', 'G', 'T']
    for i in range(1, 5):
        count[ele[i]] += count[ele[i-1]]
    for j in range(len(s) - 1, -1, -1):
        c = s[j]
        count[c] -= 1
        order[count[c]] = j
    return order

def compute_character_classes(text,order):
  n = len(text)
  classes = [0]*n
  classes[order[0]] = 0
  for i in range(1,n):
    if text[order[i]] == text[order[i-1]]:
      classes[order[i]] = classes[order[i-1]] 
    else:
      classes[order[i]] = classes[order[i-1]] + 1
  return classes

def sort_doubled(text, L, order, classes):
  n = len(text)
  count = [0]*n
  new_order = [0]*n
  for i in range(n):
    count[classes[i]] += 1
  for j in range(1,n):
    count[j] += count[j-1]
  for j in range(n-1,-1,-1):
    start = (order[j] - L + n) % n
    cl = classes[start]
    count[cl] -=  1
    new_order[count[cl]] = start 
  return new_order

def update_classes(new_order, classes, L):
  n = len(new_order)
  new_classes = [0]*n
  new_classes[new_order[0]] = 0
  for i in range(1,n):
    cur = new_order[i]
    prev = new_order[i-1]
    mid = (cur + L) % n
    mid_prev = (prev + L) % n
    if classes[cur] == classes[prev] and classes[mid] == classes[mid_prev]:
      new_classes[cur] = new_classes[prev] 
    else:
      new_classes[cur] = new_classes[prev] + 1

  return new_classes

def build_suffix_array(text):
  order = SortCharacters(text)
  classes =  compute_character_classes(text,order)

  L = 1

  while L < len(text):
    order = sort_doubled(text, L, order, classes)
    classes = update_classes(order, classes, L)
    L = 2*L
  
  return order


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
