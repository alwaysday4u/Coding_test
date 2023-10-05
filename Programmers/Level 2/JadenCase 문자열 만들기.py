'''
https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''

import re
def solution(s):
    L=re.split(r'( )',s)
    L2=[]
    for i in L:
        if re.findall('[0-9]+', i):
            L2.append(i.lower())
        else:
            L2.append(i.title())
    return ''.join(L2)
