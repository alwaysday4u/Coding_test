'''
https://school.programmers.co.kr/learn/courses/30/lessons/12914
'''

def solution(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        answer = {1:1, 2:2}
        for i in range(3,n+1):
            answer[i]=answer[i-1]+answer[i-2]
    return answer[n]%1234567
