'''
https://school.programmers.co.kr/learn/courses/30/lessons/17680
'''

from collections import deque

def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = deque([])
    answer = 0
    for i in cities:
        if cacheSize:
            if i in cache:
                cache.remove(i)
                cache.append(i)
                answer +=1
            else:
                if len(cache)>=cacheSize:
                    cache.popleft()
                cache.append(i)
                answer+=5
        else:
            answer = 5*len(cities)
                
    return answer
