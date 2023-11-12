'''
https://school.programmers.co.kr/learn/courses/30/lessons/49994
'''

def solution(dirs):
    x, y = 0, 0
    D = {'U': (0,1), 'D': (0,-1), 'L': (-1, 0), 'R': (1, 0)}
    s = set()
    for i in list(dirs):
        dx, dy = D[i]
        nx = x + dx
        ny = y + dy
        if -5<=nx<=5 and -5<=ny<=5:
            s.add(((x,y),(nx, ny)))
            s.add(((nx,ny),(x,y)))
            y = ny
            x = nx
    return len(s)//2
