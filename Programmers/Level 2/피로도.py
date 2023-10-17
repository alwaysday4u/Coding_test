'''
https://school.programmers.co.kr/learn/courses/30/lessons/87946
'''

from collections import deque

def bfs(start, k, graph):
    queue = deque()
    queue.append([start, k, 0, [False for _ in range(len(graph))]])
    cntList = []
    
    while queue:
        location, stamina, cnt, visited = queue.popleft()
        visited[location] = True
        stamina -= graph[location][1]
        cnt += 1
        cntList.append(cnt)
        
        for i in range(len(graph)):
            if not visited[i] and stamina >= graph[i][0]:
                queue.append([i, stamina, cnt, visited[:]])
                
    return max(cntList)

def solution(k, dungeons):
    ans = 0
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            ans = max(ans, bfs(i, k, dungeons))
    return ans
