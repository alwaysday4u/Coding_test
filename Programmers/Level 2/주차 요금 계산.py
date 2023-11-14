'''
https://school.programmers.co.kr/learn/courses/30/lessons/92341
'''

import math

def solution(fees, records):
    answer = []
    D = dict()
    for i in records:
        t, c, _ = map(str, i.split())
        if c in D.keys():
            D[c].append(t)
        else:
            D[c]=[t]
    tList = []
    D= dict(sorted(D.items()))
    for c in D.keys():
        if len(D[c]) % 2:
            D[c].append("23:59")
    for c in D.keys():
        cnt = 0
        time = D[c]
        for idx in range(0,len(time),2):
            it1, it2 = map(int, time[idx].split(':'))
            ot1, ot2 = map(int, time[idx+1].split(':'))
            cnt += (ot1-it1)*60 + (ot2-it2)
        tList.append(cnt)
    w, x, y, z = map(int, fees)
    for i in tList:
        if i<=w:
            answer.append(x)
        else:
            answer.append(x+math.ceil((i-w)/y)*z)
        
    return answer
