'''
https://school.programmers.co.kr/learn/courses/30/lessons/12973
'''

def solution(s):
    L=[]
    for i in s:
        L.append(i)
        if len(L)>1 and L[-1]==L[-2]:
            del L[-1]
            del L[-1]
    return 0 if L else 1
