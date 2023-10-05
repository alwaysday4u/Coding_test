'''
https://school.programmers.co.kr/learn/courses/30/lessons/12980
'''

def solution(n):
    ans = 0
    while n:
        if n%2:
            n-=1
            ans+=1
        n=n//2
    return ans
