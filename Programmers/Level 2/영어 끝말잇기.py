'''
https://school.programmers.co.kr/learn/courses/30/lessons/12981
'''

def solution(n, words):
    answer=[0,0]
    L=[]
    for i in range(len(words)):
        L.append(words[i])
        s=set(L)
        if len(L)!=len(s):
            answer = [i%n+1,i//n+1]
            break
        if i>0 and words[i-1][-1]!=words[i][0]:
            answer = [i%n+1,i//n+1]
            break
    return answer
