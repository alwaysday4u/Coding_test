'''
https://blog.naver.com/alwaysday4u/223254446549
'''

from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    cnt=0
    cntMax = len(queue1) + len(queue2)
    if (s1+s2)%2:
        return -1
    while s1!=s2:
        if cnt>=cntMax:
            return -1
        while queue2 and s1<s2:
            n=queue2.popleft()
            queue1.append(n)
            s1+=n
            s2-=n
            cnt+=1
        while queue1 and s1>s2:
            n=queue1.popleft()
            queue2.append(n)
            s1-=n
            s2+=n
            cnt+=1
    return cnt
