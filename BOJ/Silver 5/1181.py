'''
https://www.acmicpc.net/problem/1181
'''

from sys import stdin
wordsList=[]

for _ in range(int(stdin.readline().strip())):
    wordsList.append(stdin.readline().strip())
wordsList=list(set(wordsList))
wordsList.sort()
wordsList.sort(key = lambda x: len(x))
for word in wordsList:
    print(word)
