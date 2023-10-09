'''
https://www.acmicpc.net/problem/1003
'''

def fibonacci_call(n):
    callDict={0: [1,0], 1:[0,1]}
    if n>1:
        for i in range(2,n+1):
            callDict[i]=[a+b for a,b in zip(callDict[i-1], callDict[i-2])]
    return callDict[n]

t=int(input())
caseList=[]
for i in range(t):
    caseList.append(int(input()))
for i in caseList:
    L=fibonacci_call(i)
    print(L[0], L[1])
