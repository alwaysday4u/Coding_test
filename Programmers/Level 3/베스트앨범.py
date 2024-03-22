'''
https://school.programmers.co.kr/learn/courses/30/lessons/42579
'''

from collections import defaultdict
def solution(genres, plays):
    L = [[i, genres[i], plays[i]] for i in range(len(genres))]
    d = defaultdict(list)
    for info in L:
        d[info[1]].append([info[0], info[2]])
    for i in d.keys():
        d[i] = sorted(d[i], key = lambda x: -x[1])
    total_cnt = sorted(d.keys(), key = lambda x: -sum([i[1] for i in d[x]]))
    answer = []
    for i in total_cnt:
        answer.extend(d[i][:2])
    answer = [i[0] for i in answer]
    return answer
