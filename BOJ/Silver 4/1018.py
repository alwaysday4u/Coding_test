'''
https://www.acmicpc.net/problem/1018
'''

import sys

n, m = map(int, input().split())
wonlae = []
cnt = []

for _ in range(n):
    wonlae.append(sys.stdin.readline().rstrip())
for x in range(n-7):
    for y in range(m-7):
        idx1 = 0
        idx2 = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2:
                    if wonlae[i][j] != 'B':
                        idx1 += 1
                    if wonlae[i][j] != 'W':
                        idx2 += 1
                else:
                    if wonlae[i][j] != 'W':
                        idx1 += 1
                    if wonlae[i][j] != 'B':
                        idx2 += 1
        cnt.append(min(idx1, idx2))

print(min(cnt))
