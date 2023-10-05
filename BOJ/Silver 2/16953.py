'''
https://www.acmicpc.net/problem/16953
'''

a, b = map(int, input().split())
n=1
while b!=a:
  n+=1
  c=b
  if b%10==1:
    b=int(b/10)
  elif b%2==0:
    b/=2
  if c==b:
    print(-1)
    break
else:
  print(n)
