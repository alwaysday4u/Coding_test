'''
https://school.programmers.co.kr/learn/courses/30/lessons/84512
'''

from itertools import product

def solution(word):
    L = []
    for i in range(1,6):
        for j in product(list('AEIOU'), repeat=i):
            L.append(''.join(list(j)))
    return sorted(L).index(word) + 1
