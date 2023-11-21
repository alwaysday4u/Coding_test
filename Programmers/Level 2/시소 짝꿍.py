'''
https://school.programmers.co.kr/learn/courses/30/lessons/152996
'''

from collections import defaultdict

def solution(weights):
    answer = 0
    d = defaultdict(int)
    for i in weights:
        answer += d[i] + d[i*2] + d[i/2] + d[(i*2)/3] + d[(i*3)/2] + d[(i*4)/3] + d[(i*3)/4]
        d[i]+=1
    return answer
