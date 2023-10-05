'''
https://www.acmicpc.net/problem/16463
'''

year=int(input())
L=[0,31,28,31,30, 31, 30, 31, 31, 30, 31, 30]
LL=[0,31,29,31,30, 31, 30, 31, 31, 30, 31, 30]
day=2
cnt=0
for i in range(2019, year+1):
  if i%400==0: #윤년
    for j in LL:
      day+=j
      if day%7==0:
        cnt+=1
  elif i%100==0: #윤년아님
    for j in L:
      day+=j
      if day%7==0:
        cnt+=1
  elif i%4==0: #윤년
    for j in LL:
      day+=j
      if day%7==0:
        cnt+=1
  else:
    for j in L:
      day+=j
      if day%7==0:
        cnt+=1
  day+=31

print(cnt)
