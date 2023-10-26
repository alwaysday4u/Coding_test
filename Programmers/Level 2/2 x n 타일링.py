'''
https://school.programmers.co.kr/learn/courses/30/lessons/12900
'''

def solution(n):
    dp = []
    for i in range(n):
        if i==0:dp.append(1)
        elif i==1:dp.append(2)
        else:dp.append((dp[i-1] + dp[i-2])%1000000007)
    return dp.pop()
