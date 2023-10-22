'''
https://www.acmicpc.net/problem/11651
'''

import sys

pntList = []
for _ in range(int(input())):
    pntList.append(list(map(int, sys.stdin.readline().rstrip().split())))
pntList.sort(key = lambda x: (x[1],x[0]))
for i in pntList:
    print(i[0], i[1])
