'''
https://school.programmers.co.kr/learn/courses/30/lessons/17687
'''

def decToNum(num, mod):
    nList = "0123456789ABCDEF"
    a, b = num//mod, num%mod
    if a:
        return decToNum(a, mod)+nList[b]
    else:
        return nList[b]

def solution(n, t, m, p):
    pList = []
    game=''
    for i in range(m*t):
        game+=str(decToNum(i,n))
    for _ in range(t):
        pList.append(game[p-1])
        p+=m
    return ''.join(pList)
