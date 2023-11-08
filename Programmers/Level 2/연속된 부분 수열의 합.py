'''
https://school.programmers.co.kr/learn/courses/30/lessons/178870
'''

def solution(sequence, k):
    answer = [0, len(sequence)]
    s, e = 0, 0
    ans = sequence[0]
    while True:
        if ans<k:
            e+=1
            if e == len(sequence):break
            ans+=sequence[e]
        else:
            if ans==k and e-s<answer[1]-answer[0]:
                answer = [s, e]
            ans-=sequence[s]
            s+=1
            
    return answer


'''
Reference:
https://velog.io/@sugyeonghh/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9Python
'''
