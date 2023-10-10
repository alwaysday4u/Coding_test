'''
https://school.programmers.co.kr/learn/courses/30/lessons/12949
'''

def solution(arr1, arr2):
    return [[sum(x*y for x, y in zip(a1, a2)) for a2 in zip(*arr2)] for a1 in arr1]
