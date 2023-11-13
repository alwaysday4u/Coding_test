'''
https://school.programmers.co.kr/learn/courses/30/lessons/42583
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    answer = 0
    on_bridge = deque([])
    while True:
        ssum = 0
        if not truck_weights and not on_bridge:
                break
        answer+=1
        if on_bridge and on_bridge[0][1]>= bridge_length:
            on_bridge.popleft()
        if on_bridge:
            for i in range(len(on_bridge)):
                on_bridge[i][1] +=1
                ssum+=on_bridge[i][0]
        if truck_weights and len(on_bridge)<bridge_length and ssum+truck_weights[0]<=weight:
                on_bridge.append([truck_weights.popleft(), 1])
           
    return answer
