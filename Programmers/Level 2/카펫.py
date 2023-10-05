'''
https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    y=1
    for i in range(1,yellow):
        if not yellow%i and brown==2*(i+(yellow/i))+4:
            y=i
            break
    L=[2+y, 2+(yellow/y)]
    return [max(L),min(L)]
