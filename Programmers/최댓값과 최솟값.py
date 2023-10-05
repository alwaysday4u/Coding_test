'''
https://school.programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    mx = str(max([int(i) for i in s.split()]))
    mn = str(min([int(i) for i in s.split()]))
    answer = mn +' '+ mx
    return answer
