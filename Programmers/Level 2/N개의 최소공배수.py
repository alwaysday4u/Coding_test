'''
https://school.programmers.co.kr/learn/courses/30/lessons/12953
'''

import math

def solution(arr):
    while len(arr)>1:
        k=(arr[-1]*arr[-2])//math.gcd(arr[-1],arr[-2])
        arr.pop()
        arr.pop()
        arr.append(k)      

    return arr[0]
