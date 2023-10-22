'''
https://www.acmicpc.net/problem/10773
'''

import sys

stack = []
for _ in range(int(input())):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))
