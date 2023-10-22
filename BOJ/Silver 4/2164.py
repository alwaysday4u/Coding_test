'''
https://www.acmicpc.net/problem/2164
'''

from collections import deque

L=deque([i+1 for i in range(int(input()))])

while L:
    n=L.popleft()
    if L:
        L.append(L.popleft())
    else:
        print(n)
        break
