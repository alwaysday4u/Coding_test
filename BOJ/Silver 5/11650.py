'''
https://www.acmicpc.net/problem/11650
'''

import sys

pointList = []
for _ in range(int(input())):
    pointList.append(list(map(int, sys.stdin.readline().rstrip().split())))
pointList.sort(key = lambda x: (x[0], x[1]))

for i in pointList:
    print(i[0], i[1])
