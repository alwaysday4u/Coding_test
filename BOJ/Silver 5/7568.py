'''
https://www.acmicpc.net/problem/7568
'''

import sys

L=[]
for _ in range(int(input())):
    L.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in L:
    rank = 1
    for j in L:

        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank, end = ' ')

