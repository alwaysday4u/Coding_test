'''
https://school.programmers.co.kr/learn/courses/30/lessons/42746
'''

def solution(numbers):
    return str(int(''.join(sorted(list(map(str, numbers)), key=lambda x : x*3,reverse = True))))
