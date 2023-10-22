''
https://school.programmers.co.kr/learn/courses/30/lessons/43165
'''

def solution(numbers, target):
    result = [0]
    idx = 0
    for i in numbers:
        caseList = []
        for j in result:
            caseList.append(j+i)
            caseList.append(j-i)
        result = caseList
                
    return caseList.count(target)
