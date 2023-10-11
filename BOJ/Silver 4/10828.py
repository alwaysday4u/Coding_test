'''
https://www.acmicpc.net/problem/10828
'''

from sys import stdin
L=[]

for _ in range(int(stdin.readline())):
    button = stdin.readline().split()
    if button[0] == 'push':
        L.append(int(button[1]))
    elif button[0] == 'empty':
        if L: print(0)
        else: print(1)
    elif button[0] == 'pop':
        if L: print(L[-1]); L.pop()
        else: print(-1)
    elif button[0] == 'top':
        if L: print(L[-1]);
        else: print(-1)
    else:
        print(len(L))
