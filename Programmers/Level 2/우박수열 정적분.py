'''
https://school.programmers.co.kr/learn/courses/30/lessons/134239
'''

def solution(k, ranges):
    answer = []
    y=[]
    while k !=1:
        y.append(k)
        if k%2:
            k*=3
            k+=1
        else:
            k/=2
    y.append(1)
    n = len(y)-1
    for i in ranges:
        a, b = i[0], n+i[1]
        print(a,b)
        if a>b:
            answer.append(-1.0)
        else:
            s = 0
            for j in range(a, b):
                s += y[j]+y[j+1]
            answer.append(s/2)  
    return answer
