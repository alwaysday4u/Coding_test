'''
https://www.acmicpc.net/problem/11399
'''

import sys

n = int(input())
L = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
ans = 0

for i in range(1,n+1):
    ans+=sum(L[:i])
print(ans)
    
