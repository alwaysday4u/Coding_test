'''
https://school.programmers.co.kr/learn/courses/30/lessons/12911
'''

def solution(n):
    answer=0
    L=list(bin(n)[2:])
    for i in range(n+1, pow(2, len(L)+1)):
        if list(bin(i)[2:]).count('1') == L.count('1'):
            answer=i
            break
    return answer
