'''
https://www.acmicpc.net/problem/1929
'''

m, n = map(int, input().split())
if m==1: m=2
for i in range(m, n+1):
    primeNumber = True
    for j in range(2, int(pow(i,0.5))+1):
        if i%j == 0:
            primeNumber = False
            break
    if primeNumber:
        print(i)
