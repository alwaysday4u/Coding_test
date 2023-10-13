'''
https://www.acmicpc.net/problem/1764
'''

import sys

n, m = map(int, input().split())
noHeard = set()
noSeek = set()

for i in range(n):
    noHeard.add(sys.stdin.readline().rstrip())
for j in range(m):
    noSeek.add(sys.stdin.readline().rstrip())

no = sorted(list(noHeard & noSeek))

print(len(no))
for i in no:
    print(i)
