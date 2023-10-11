'''
https://www.acmicpc.net/problem/9012
'''

for _ in range(int(input())):
    s=input()
    while s:
        s2=s
        s=s.replace('()','')
        if len(s)==0:
            print("YES")
        if s2==s:
            print("NO")
            break
