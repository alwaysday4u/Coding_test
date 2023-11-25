'''
https://school.programmers.co.kr/learn/courses/30/lessons/42860#
'''

def solution(name):
    alpha_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_dict = {i:min(j, 26-j) for j, i in enumerate(alpha_str)}
    answer = 0
    move = len(name)-1
    for i, j in enumerate(name):
        answer+=alpha_dict[j]
        cnt = i + 1
        while cnt < len(name) and name[cnt] == 'A':
            cnt += 1
        move = min([move, 2*i+len(name)-cnt, i+2*(len(name)-cnt)])
    return answer + move
