'''
https://school.programmers.co.kr/learn/courses/30/lessons/131704
'''

def solution(order):
    ans = 0  
    stack = []
    
    for i in range(len(order)):
        stack.append(i+1)
        while stack and stack[-1]==order[ans]:
            ans+=1
            stack.pop()
            if len(stack)==0:
                break

    return ans
