'''
https://school.programmers.co.kr/learn/courses/30/lessons/64065
'''

from collections import Counter
import re

def solution(s):
    return [i[0] for i in Counter([int(i) for i in re.sub("({|})","",s).split(',') ]).most_common()]
