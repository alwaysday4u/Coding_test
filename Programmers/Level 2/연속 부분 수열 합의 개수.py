'''
https://school.programmers.co.kr/learn/courses/30/lessons/131701
'''

def solution(elements):
    answer = 0
    L=[]
    a=sum(elements)
    element=elements*2
    L.append(a)
    for i in range(len(elements)):
        for j in range(len(elements)):
            L.append(sum(element[i:i+j+1]))
    s=set(L)
    answer = len(s)
    return answer
