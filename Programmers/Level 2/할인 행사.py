'''
https://school.programmers.co.kr/learn/courses/30/lessons/131127
'''

from collections import Counter
def solution(want, number, discount):
    answer = 0
    goodsList=dict()
    for i,j in zip(want, number):
        goodsList[i] = j
    for i in range(len(discount)-9):
        if goodsList == Counter(discount[i:i+10]):
            answer +=1
    return answer
