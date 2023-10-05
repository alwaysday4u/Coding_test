'''
https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer=True
    cnt0, cnt1 = 0,0
    for i in list(s):
        if i=='(': cnt0+=1
        else: cnt1+=1
        if cnt0<cnt1:
            answer = False
            break;
        answer=False if cnt0!=cnt1 else True
    return answer
