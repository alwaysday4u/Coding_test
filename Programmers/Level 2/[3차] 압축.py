'''
https://school.programmers.co.kr/learn/courses/30/lessons/17684
'''

def solution(msg):
    answer = []
    wordDict = dict([(j,i+1) for i, j in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))])
    w = 0
    c = 0
    
    while True:
        c+=1
        if c == len(msg):
            answer.append(wordDict[msg[w:c]])
            break
        if msg[w:c+1] not in wordDict.keys():
            wordDict[msg[w:c+1]] = len(wordDict) + 1
            answer.append(wordDict[msg[w:c]])
            w = c
    return answer
