'''
https://school.programmers.co.kr/learn/courses/30/lessons/172927
reference: https://kcw0360.tistory.com/5#%3CCode%3E-1
'''

def solution(picks, minerals):
    answer = 0
    minerals = minerals[:sum(picks)*5]
    L = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    idx, cnt = 0, 0
    mineral_cnt = []
    tired = [0,0,0]
    
    while idx < len(minerals):
        if cnt == 5:
            mineral_cnt.append(tired)
            cnt=0
            tired=[0,0,0]
        if minerals[idx]=='diamond':
            tired[0]+=1
        elif minerals[idx]=='iron':
            tired[1]+=1
        else:
            tired[2]+=1
        idx+=1
        cnt+=1
    
    mineral_cnt.append(tired)
    mineral_cnt.sort(key=lambda x: (x[0],x[1],x[2]), reverse = True)
    
    pick = []
    for i in range(3):
        pick+=[i]*picks[i]
    pick_idx=0
    for i in range(len(mineral_cnt)):
        for j in range(3):
            answer+= L[pick[pick_idx]][j] * mineral_cnt[i][j]
        pick_idx+=1

    return answer
