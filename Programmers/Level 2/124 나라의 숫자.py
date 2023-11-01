'''
https://school.programmers.co.kr/learn/courses/30/lessons/12899
'''

def convert124(n):
    s=''
    while n:
        if n%3:
            s+= str(n%3)
            n= int(n/3)
        else:
            s+='4'
            n = int(n/3) - 1
    return s[::-1]
            
def solution(n):
    return convert124(n)
