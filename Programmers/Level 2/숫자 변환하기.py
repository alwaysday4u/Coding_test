'''
https://school.programmers.co.kr/learn/courses/30/lessons/154538
'''

def solution(x, y, n):
    import math
    
    if x == y:
        return 0
    dp = [math.inf]*(y+1)
    dp[x] = 0
    
    for i in range(x, y+1):
        if dp[i] == math.inf:
            continue       
        if y>=i+n:
            dp[i+n] = min(dp[i]+1, dp[i+n])
        if y>=i*2:
            dp[i*2] = min(dp[i]+1, dp[i*2])
        if y>=i*3:
            dp[i*3] = min(dp[i]+1, dp[i*3])
    
    return dp[y] if dp[y]!=math.inf else -1
