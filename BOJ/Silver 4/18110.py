'''
https://www.acmicpc.net/problem/18110
'''

import sys

def round_new(num):
    return int(num) + (1 if num-int(num) >=0.5 else 0)

t = int(input())
r = round_new(t*0.15)

if t:
    levelList = []
    for _ in range(t):
        levelList.append(int(sys.stdin.readline()))
    levelList.sort()
    print(round_new(sum(levelList[r:len(levelList)-r])/(t-2*r)))
else:
    print(0)
