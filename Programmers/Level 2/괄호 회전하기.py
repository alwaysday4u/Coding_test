'''
https://school.programmers.co.kr/learn/courses/30/lessons/76502
'''

def solution(s):
    answer = 0
    for i in range(len(s)):
        s2=s[i:]+s[:i]
        while True:
            L=len(s2)
            s2=s2.replace("()",'')
            s2=s2.replace("[]",'')
            s2=s2.replace("{}",'')
            L2=len(s2)
            if L==L2:
                break
            elif L2==0:
                answer+=1
                break
    return answer
