'''
https://school.programmers.co.kr/learn/courses/30/lessons/12946
'''

def solution(n):
    L = []
    def hanoi(n, pos1=1, pos2=3, pos3=2):
        if n == 1:L.append([pos1, pos2])
        else:
            hanoi(n-1, pos1, pos3, pos2)
            hanoi(1, pos1, pos2, pos3)
            hanoi(n-1, pos3, pos2, pos1)
    hanoi(n)
    return L
