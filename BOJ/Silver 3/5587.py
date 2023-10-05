'''
https://www.acmicpc.net/problem/5587
'''

L=[]
n=int(input())
for i in range(n):
  L.append(int(input()))
L2=[i for i in range(1,2*n+1) if i not in L]
L.sort()

a, b = 0,0
k=0
while True:
  for i in L:
    if max(L)<k:
      k=0
      break
    if k==0:
      k=min(L)
      L.remove(min(L))
      break
    if i>k:
      L.remove(i)
      k=i
      break
  if not L:
    a=len(L2)
    break
  for i in L2:
    if max(L2)<k:
      k=0
      break
    if k==0:
      k=min(L2)
      L2.remove(min(L2))
      break
    if i>k:
      L2.remove(i)
      k=i
      break
  if not L2:
    b=len(L)
    break
    
print(a)
print(b)
