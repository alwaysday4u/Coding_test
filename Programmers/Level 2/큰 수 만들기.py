'''
https://school.programmers.co.kr/learn/courses/30/lessons/42883
'''

def solution(number, k):
    L = []
    cnt = 0
    for i in number:
        while L and L[-1] < i and cnt < k:
            cnt+=1
            L.pop()
        L.append(i)
    if cnt < k:
        L = L[:-k]
    return ''.join(L)
