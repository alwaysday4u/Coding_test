'''
https://www.acmicpc.net/problem/3135
'''

L=[]
Labs=[]
count=0
a,b = map(int, input().split())
n=int(input())
for i in range(n):
  num = int(input())
  L.append(num)
  #Labs.append(abs(b-num))
Labs.append(abs(a-b))

for i in L:
  Labs.append(abs(b-i))
m=min(Labs)
if m!=Labs[0]:
  count+=1
count+=m
print(count)
