'''
https://www.acmicpc.net/problem/1300
'''

def binary_search(target, start, end):
    while start<=end:
        mid = (start + end) // 2
        cnt=0
        for i in range(1, n+1):
            cnt+=min(mid//i, n)
        if cnt>=target:
            end = mid - 1
        else:
            start = mid + 1
    return start
n=int(input())
k=int(input())
print(binary_search(k, 1, k))
