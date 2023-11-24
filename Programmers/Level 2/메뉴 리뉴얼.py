'''
https://school.programmers.co.kr/learn/courses/30/lessons/72411
'''

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for j in course:
        L = []
        for i in orders:
            L+=list(combinations(sorted(i), j))
        d=Counter(L).most_common()
        answer+= [k for k, v in d if v > 1 and v == d[0][1]]
    return sorted([''.join(i) for i in answer])
