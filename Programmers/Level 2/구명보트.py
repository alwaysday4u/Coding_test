'''
https://school.programmers.co.kr/learn/courses/30/lessons/42885
'''

def solution(people, limit):
    i=0
    j=len(people)-1
    answer=0
    people.sort()
    while i<j:
        if people[i]+people[j]<=limit:
            i+=1
            answer+=1
        j-=1
    return len(people)-answer
