'''
https://www.acmicpc.net/problem/2839
'''

dp = [-1]*5004
dp[3]=1
dp[5]=1

n = int(input())
for i in range(6, n+1):
    if dp[i-3] != -1 and dp[i-5] !=-1:
        dp[i] = min(dp[i-3], dp[i-5]) + 1
    elif dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1

print(dp[n])
