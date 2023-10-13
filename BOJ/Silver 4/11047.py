'''
https://www.acmicpc.net/problem/11047
'''

import sys

n, k = map(int, input().split())
coinList = []
ans = 0

for _ in range(n):
    coinList.append(int(sys.stdin.readline().rstrip()))
coinList.sort(reverse = True)

for i in coinList:
    if k//i:
        ans+= k//i
        k=k%i
print(ans)
