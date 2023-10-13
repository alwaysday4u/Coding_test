'''
https://www.acmicpc.net/problem/17219
'''

import sys

n, m = map(int, input().split())
passwordList=dict()

for i in range(n):
    L = sys.stdin.readline().rstrip().split()
    passwordList[L[0]] = L[1]
for i in range(m):
    site = sys.stdin.readline().rstrip()
    print(passwordList[site])
    
