'''
https://school.programmers.co.kr/learn/courses/30/lessons/176962
'''

from collections import deque
def solution(plans):
    answer = []
    temp = []
    stop = []
    plans=deque(sorted(plans, key = lambda x: x[1]))
    
    while len(plans)>1:
        now = plans.popleft()
        name = now[0]
        starth, startm = map(int, now[1].split(':'))
        start = starth*60 + startm
        playtime = int(now[2])
        nexth, nextm = map(int, plans[0][1].split(':'))
        nexts = nexth*60+nextm
        t = nexts - (start+playtime)
        if t<0:
            stop.append([name, playtime-(nexts-start)])
        else:
            answer.append(name)
            while t>0 and stop:
                if t < stop[-1][1]:
                    stop[-1][1] -= (nexts-(start+playtime))
                    break
                else:
                    t -= stop[-1][1]
                    answer.append(stop.pop()[0])
    answer.append(plans.pop()[0])
    answer.extend(name for name, playtime in reversed(stop))
    return answer
