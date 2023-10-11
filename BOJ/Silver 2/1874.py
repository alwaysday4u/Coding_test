'''
https://www.acmicpc.net/problem/1874
'''

cnt = 1
stack = []
opt = []
isTrue=True

for i in range(int(input())):
    num = int(input())
    while cnt<=num:
        stack.append(cnt)
        opt.append('+')
        cnt+=1
    if stack[-1]==num:
        stack.pop()
        opt.append('-')
    else:
        isTrue = False
        break

if isTrue:
    for i in opt:
        print(i)
else:
    print('NO')
