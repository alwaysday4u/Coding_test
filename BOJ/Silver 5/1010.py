'''
https://www.acmicpc.net/problem/1010
'''

import sys

for i in range(int(input())):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dp=[[0 for k in range(j+1)] for j in range(b+1)]
    dp[0][0] = 1
    for j in range(1, b+1):
        for k in range(j+1):
            if k == 0:
                dp[j][k] = 1
            elif k == j:
                dp[j][k] = 1
            else:
                dp[j][k] = dp[j-1][k-1] + dp[j-1][k]
    print(dp[b][a])
