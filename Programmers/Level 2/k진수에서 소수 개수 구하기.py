'''
https://school.programmers.co.kr/learn/courses/30/lessons/92335
'''

import math

def decToK(num, d, L =[]):
    a = num // d
    b = num % d
    L.append(str(b))
    if a :
        return decToK(a, d)
    else :
        return ''.join(L[::-1])

def findPrimeNum(numberList):
    numberList = [i for i in numberList if i]
    cnt = len(numberList)
    if cnt:
        for i in numberList:
            i = int(i)
            if i>1:
                for j in range(2, int(math.sqrt(i))+1):
                    if not i % j:
                        cnt-=1
                        break
            else:
                cnt-=1
    return cnt
    
def solution(n, k):
    return findPrimeNum(decToK(n, k).split('0'))
