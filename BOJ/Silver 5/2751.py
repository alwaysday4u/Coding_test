'''
https://www.acmicpc.net/problem/2751
'''

import sys

numList = []
for _ in range(int(input())):
    numList.append(int(sys.stdin.readline().rstrip()))
numList.sort()
for i in numList:
    print(i)
