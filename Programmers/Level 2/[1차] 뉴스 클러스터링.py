'''
https://school.programmers.co.kr/learn/courses/30/lessons/17677
'''

from collections import Counter

def solution(str1, str2):
    L1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    L2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    if not L1 and not L2:
        return 65536
    else:
        c1 = Counter(L1)
        c2 = Counter(L2)
        return int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
