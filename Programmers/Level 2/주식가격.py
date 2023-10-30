'''
https://school.programmers.co.kr/learn/courses/30/lessons/42584
'''

from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while len(prices)>1:
        s = prices.popleft()
        t=0
        for i in prices:
            t+=1
            if i<s:
                break
        answer.append(t)
    answer.append(0)
                    
    return answer
