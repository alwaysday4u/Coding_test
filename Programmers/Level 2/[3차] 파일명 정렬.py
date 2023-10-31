'''
https://school.programmers.co.kr/learn/courses/30/lessons/17686
'''

def hnt(s):
    idx_s=0
    for i in range(len(s)):
        if s[i] and s[i].isdigit():
            idx_s=i
            break
    idx_e=idx_s+1
    for i in range(idx_s+1,len(s)):
        if not s[i] or s[i].isdigit():
            idx_e+=1
        else:
            break          
    return (s[:idx_s], s[idx_s:idx_e], s[idx_e:])

def solution(files):
    answer = sorted([hnt(i) for i in files], key = lambda x: (x[0].upper(), int(x[1])))
    return [''.join(i) for i in answer]
