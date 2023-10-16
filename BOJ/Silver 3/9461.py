'''

'''

import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    dp=[0]*(n+1)
    for j in range(1,n+1):
        if j<3:
            dp[j]=1
        else:
            dp[j] = dp[j-3]+dp[j-2]
    print(dp[n])
