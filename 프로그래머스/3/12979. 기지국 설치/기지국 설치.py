import math

def solution(n, stations, w):
    answer = 0
    r = w*2+1
    start = 0
    uncovered = []
    for s in stations:
        uncovered.append((start, s-w-1))
        start = s+w
    if start!=n+1:
        uncovered.append((start, n))
    for a,b in uncovered:
        count = b-a
        answer += math.ceil(count/r)
    return answer