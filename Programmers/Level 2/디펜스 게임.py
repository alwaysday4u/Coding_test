'''
https://school.programmers.co.kr/learn/courses/30/lessons/142085
'''

from heapq import heappop, heappush

def solution(n, k, enemy):
    h = []
    for i, e in enumerate(enemy):
        heappush(h,e)
        print(h)
        if len(h) > k:
            n-=heappop(h)
        if n<0:
            return i
    return len(enemy)
