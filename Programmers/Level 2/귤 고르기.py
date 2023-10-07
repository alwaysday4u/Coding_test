'''
https://school.programmers.co.kr/learn/courses/30/lessons/138476
'''

def solution(k, tangerine):
    tangerine_size=dict()
    for i in set(tangerine):
        tangerine_size[i]=0
    for i in tangerine:
        tangerine_size[i]+=1
    result=0
    for i in sorted(tangerine_size.values(),reverse=True):
        k-=i
        result+=1
        if k<=0:
            break
    return result
