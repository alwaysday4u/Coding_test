'''
https://www.acmicpc.net/problem/1966
Algorithm Reference: https://hongcoding.tistory.com/42
'''

import sys
from collections import deque

ansList = []
for _ in range(int(input())):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    cnt=0
    while queue:
        mostImportant = max(queue)
        front = queue.popleft()
        m-=1

        if front == mostImportant:
            cnt+=1
            if m<0:
                ansList.append(cnt)
                break
        else:
            queue.append(front)
            if m<0:
                m = len(queue)-1

for i in ansList:
    print(i)
