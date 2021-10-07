# python3
import sys


def prefix_function(s):
  n = len(s)
  pi = [0]*n
  j = 0
  for i in range(1,n):
    while j>0 and s[i] != s[j]:
      j = pi[j-1]
    if s[i] == s[j]:
      j += 1
    else:
      j = 0
    pi[i] = j
  return pi

def find_pattern(pattern, text):
  s = pattern + '$' + text
  prefix = prefix_function(s)
  result = []
  for i in range(len(pattern)+1, len(s)):
    if prefix[i] == len(pattern):
      result.append(i-2*len(pattern))     
  return result


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

