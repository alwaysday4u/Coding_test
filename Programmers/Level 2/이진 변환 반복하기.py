'''
https://school.programmers.co.kr/learn/courses/30/lessons/70129
'''

def solution(s):
    result=list(s)
    cnt, cnt0 = 0,0
    while True:
        l=len(result)
        if l==1:
            break
        #0 제거
        cnt0+=result.count('0')
        result=list(bin(result.count('1')))[2:]
        cnt+=1
    return [cnt, cnt0]
