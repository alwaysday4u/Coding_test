'''
https://www.acmicpc.net/problem/1260
'''

from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v=queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, k = map(int, input().split())
L=[[] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)
    L[a].sort()
    L[b].sort()


visited = [False] * (n+1)
dfs(L,k,visited)
print("")
visited = [False] * (n+1)
bfs(L,k,visited)
