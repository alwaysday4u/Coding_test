'''
https://school.programmers.co.kr/learn/courses/30/lessons/42586
'''

import math

def solution(progresses, speeds):
    answer=[]
    dueDate = [math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]
    ans = 0
    for i in range(len(dueDate)):
        if dueDate[i] > dueDate[ans]:
            answer.append(i - ans)
            ans = i
    answer.append(len(dueDate)-ans)     
    return answer
