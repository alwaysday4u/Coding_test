'''
https://school.programmers.co.kr/learn/courses/30/lessons/42626
'''

import heapq

def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville)
    while len(scoville) > 1 :
        m1 = heapq.heappop(scoville) 
        if m1 >= K:
            return cnt
        else:
            m2 = heapq.heappop(scoville) 
            heapq.heappush(scoville, m1 + m2*2)
            cnt+=1
    if scoville[0]>=K:
        return cnt
    else:
        return -1
