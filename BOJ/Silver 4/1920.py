'''
https://www.acmicpc.net/problem/1920
'''

def binary_search(array, target, start, end):
    if start>end:
        return 0
    mid = (start + end)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


L=[]
n= int(input())
L = sorted(map(int, input().split()))
m = int(input())
L2 = map(int, input().split())
for i in L2:
    print(int(binary_search(L, i, 0, len(L)-1)!=0))
