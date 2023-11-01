'''
https://school.programmers.co.kr/learn/courses/30/lessons/135807
'''

from math import gcd

def solution(arrayA, arrayB):
    answer = [0]
    gcdA, gcdB = arrayA[0], arrayB[0]
    cntA, cntB = 0, 0
    for i in arrayA:
        gcdA = gcd(gcdA, i)
    for i in arrayB:
        gcdB = gcd(gcdB, i)
        
    for i in arrayA:
        if i%gcdB:
            cntA+=1
        else:
            break
    if cntA == len(arrayA):
        answer.append(gcdB)
    for i in arrayB:
        if i%gcdA:
            cntB+=1
        else:
            break
    if cntB == len(arrayB):
        answer.append(gcdA)
  
    return max(answer)
