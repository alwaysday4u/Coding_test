'''
https://www.acmicpc.net/problem/2606
'''

from collections import deque
import sys


def bfs(graph, start, visited):
    cntList = 0
    queue = deque([start])
    visited[start] = True
    while queue:
        v=queue.popleft()
        cntList+=1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cntList - 1

L= [[] for _ in range(int(input())+1)]
for i in range(int(input())):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    L[x].append(y)
    L[y].append(x)

visited_1 = [False] * len(L) 
print(bfs(L, 1, visited_1))
