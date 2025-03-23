from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bl = bridge_length
    tw = deque(truck_weights)
    onbridge = deque([])
    curw8 = 0
    while tw or onbridge:
        answer += 1
        if onbridge and onbridge[0][0]==answer:
            curw8 -= onbridge.popleft()[1]
        if tw and curw8+tw[0]<=weight:
            truck = tw.popleft()
            onbridge.append((answer+bl,truck))
            curw8 += truck
    return answer