'''
https://school.programmers.co.kr/learn/courses/30/lessons/42587
'''

from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    order = location
    answer = 1
    while priorities:
        n = priorities.popleft()
        if priorities and n < max(priorities):
            priorities.append(n)
            if order == 0:
                order = len(priorities)-1
            else:
                order -= 1
        else:
            if order == 0:
                break
            else:
                order-=1
                answer+=1

    return answer
