'''
https://school.programmers.co.kr/learn/courses/30/lessons/12924
'''

def solution(n):
    answer = 1
    for i in range(1, n//2+1):
        k=0
        for j in range(i,n):
            k+=j
            if k==n:
                answer+=1
            if k>n:
                break
    return answer
