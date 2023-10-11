'''
https://www.acmicpc.net/problem/10845
'''

from sys import stdin
from collections import deque
L=deque(list())

for _ in range(int(stdin.readline())):
    button = stdin.readline().split()
    if button[0] == 'push':
        L.append(int(button[1]))
    elif button[0] == 'front':
        if L: print(L[0])
        else: print(-1)
    elif button[0] == 'back':
        if L: print(L[-1])
        else:print(-1)
    elif button[0] == 'empty':
        if L: print(0)
        else: print(1)
    elif button[0] == 'pop':
        if L: print(L[0]); L.popleft()
        else: print(-1)
    else:
        print(len(L))
