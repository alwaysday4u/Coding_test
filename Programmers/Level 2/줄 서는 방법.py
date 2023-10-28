'''
https://school.programmers.co.kr/learn/courses/30/lessons/12936
'''

def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    answer = []
    numList = [i for i in range(1, n+1)]
    while n:
        idx, k = divmod(k,factorial(n-1))
        if k: answer.append(numList.pop(idx))
        else: answer.append(numList.pop(idx-1))
        n-=1
    return answer
