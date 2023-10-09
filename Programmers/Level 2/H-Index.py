'''
https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    citations.sort(reverse = True)
    answer = 0
    for j in range(len(citations)+1):
        k = 0
        for i in citations:
            if i>=j:
                k+=1
        if k<j:
            break
        else:
            answer=j
                
    return answer
