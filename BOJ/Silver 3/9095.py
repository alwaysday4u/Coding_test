'''
https://www.acmicpc.net/problem/9095
'''

import sys

cntDict= {1:1, 2:2, 3:4}
L=[]
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    if n>3:
        for i in range(4, n+1):
            cntDict[i] = cntDict[i-1] + cntDict[i-2] + cntDict[i-3]
    L.append(cntDict[n])

for i in L:
    print(i)
