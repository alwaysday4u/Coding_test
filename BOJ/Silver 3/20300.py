'''
https://www.acmicpc.net/problem/20300
'''

from collections import deque

n=int(input())
L=deque(sorted(map(int, input().split())))
health=[]
if n%2:
    health.append(L[-1])
    L.pop()
while L:
    health.append(int(L[0]+L[-1]))
    L.pop()
    L.popleft()
print(max(health))
