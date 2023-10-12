'''
https://www.acmicpc.net/problem/10814
'''

import sys

userList = []
for _ in range(int(input())):
    age, name = sys.stdin.readline().rstrip().split()
    userList.append([int(age), name])
for i in sorted(userList, key = lambda x: x[0]):
    print(i[0], i[1])
