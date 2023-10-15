'''
https://www.acmicpc.net/problem/11724
'''

from collections import deque
import sys

def bfs(graph, start, visited):
    queue = deque([start])
    L=[]
    visited[start] = True
    while queue:
        v=queue.popleft()
        L.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return L

cnt = 0
n, m = map(int, input().split())
graphList = [[] for _ in range(n+1)]
edgeList=[i for i in range(1, n+1)]
visitedList = [False for _ in range(n+1)]

for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  graphList[x].append(y)
  graphList[y].append(x)

while edgeList:
  startEdge = edgeList[0]
  connection = bfs(graphList, startEdge, visitedList)
  for i in connection:
    edgeList.remove(i)
  cnt+=1

print(cnt)
