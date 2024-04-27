'''
https://www.acmicpc.net/problem/1806
'''

l, n = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
ans = l + 1
s = 0

while end < len(arr):
    s += arr[end]
    while s >= n:
        s -= arr[start]
        ans = min(ans, end - start + 1)
        start += 1
    end += 1

if ans == l + 1:
    print(0)
else:
    print(ans)
