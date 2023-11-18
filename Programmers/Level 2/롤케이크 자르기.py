'''
https://school.programmers.co.kr/learn/courses/30/lessons/132265
'''

from collections import Counter

def solution(topping):
    a= set()
    b = Counter(topping)
    answer = 0
    for i in topping:
        a.add(i)
        b[i]-=1
        if b[i]==0:
            del[b[i]]
        if len(a)==len(b):
            answer+=1
    return answer
