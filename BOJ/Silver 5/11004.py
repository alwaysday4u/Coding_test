'''
https://www.acmicpc.net/problem/11004
'''

n, k = map(int, input().split())
nList = sorted(list(map(int, input().split())))
print(nList[k-1])
