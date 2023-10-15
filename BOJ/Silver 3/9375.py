'''
https://www.acmicpc.net/problem/9375
'''

from collections import Counter
import sys


for _ in range(int(input())):
    D = dict()
    for _ in range(int(input())):
        clothes = sys.stdin.readline().rstrip().split()[1]
        if clothes in D:
            D[clothes]+=1
        else:
            D[clothes] = 1

    answer = 1
    for i in D.values():
        answer *= (i+1)

    print(answer - 1)
