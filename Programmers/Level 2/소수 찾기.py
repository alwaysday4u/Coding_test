'''
https://school.programmers.co.kr/learn/courses/30/lessons/42839
'''

from itertools import permutations
import math

def primenumber(x):
    if x<2:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
    	    if not x % i:
        	    return False
        return True	

def solution(numbers):
    cnt = 0
    caseList = []
    for i in range(1, 1+len(numbers)):
        caseList+=[int(''.join(i)) for i in set(list(permutations(numbers, i)))]
    for i in set(caseList):
        if primenumber(i):
            cnt+=1
    return cnt
