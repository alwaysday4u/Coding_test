'''
https://www.acmicpc.net/problem/1620
'''

import sys

n, m = map(int, input().split())
pokemonName=dict()
for i in range(n):
    pokemonName[sys.stdin.readline().rstrip()]=i+1
pokemonNum = {v:k for (k,v) in pokemonName.items()}

for i in range(m):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdecimal() == True:
        print(pokemonNum[int(quiz)])
    else:
        print(pokemonName[quiz])
