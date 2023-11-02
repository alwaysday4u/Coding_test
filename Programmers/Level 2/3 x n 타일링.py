'''
https://school.programmers.co.kr/learn/courses/30/lessons/12902
'''

def solution(n):
    dp = [0]*(n+1)
    if n%2:
        return 0
    else:
        for i in range(n+1):
            if i==2:
                dp[i]=3
            elif i==4:
                dp[i]=11
            else:
                dp[i] = 4*dp[i-2]-dp[i-4]%1000000007

        return dp[n]%1000000007
