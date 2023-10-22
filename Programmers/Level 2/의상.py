'''
https://school.programmers.co.kr/learn/courses/30/lessons/42578
'''

from collections import Counter

def solution(clothes):
    L = list(Counter([i[1] for i in clothes]).values())
    answer = 1
    for i in L:
        answer*=(i+1)
    return answer - 1
