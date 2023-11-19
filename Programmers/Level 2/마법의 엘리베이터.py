'''
https://school.programmers.co.kr/learn/courses/30/lessons/148653
'''

def solution(storey):
    answer = 0
    while storey:
        cnt = storey % 10
        if cnt==5 and int(storey/10)%10>4 or cnt>5:
            storey+=10-cnt
        answer+=min(cnt, 10-cnt)
        storey//=10
    return answer
