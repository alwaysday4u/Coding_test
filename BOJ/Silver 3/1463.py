'''
https://www.acmicpc.net/problem/1463
'''

x = int(input())
dp = [0] * (x+1)
for i in range(2, x+1):
    L=[dp[i-1]]
    if i%3==0:
        L.append(dp[i//3])
    if i%2==0:
        L.append(dp[i//2])
    dp[i] = min(L) + 1

print(dp[x])
