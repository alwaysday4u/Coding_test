'''
https://www.acmicpc.net/problem/20529
'''

from itertools import combinations

def diff(x,y):
  return len(set(x).difference(set(y)))

for _ in range(int(input())):
  n = int(input())
  mbti = input().split()
  if n > 32:
      print(0)
  else:
    L=[]
    for a, b, c in combinations(mbti, 3):
      L.append(sum([diff(a,b), diff(b,c), diff(c, a)]))
    print(L)
    print(min(L))
