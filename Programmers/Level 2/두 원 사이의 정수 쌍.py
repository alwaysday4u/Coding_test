'''
https://school.programmers.co.kr/learn/courses/30/lessons/181187
'''

import math

def solution(r1, r2):
    ans = 0
    for i in range(1, r2+1):
        ymax = int(math.sqrt(r2**2-i**2))
        ymin = 0 if i>r1 else math.ceil(math.sqrt(r1**2-i**2))
        ans += ymax-ymin+1
    return ans*4
