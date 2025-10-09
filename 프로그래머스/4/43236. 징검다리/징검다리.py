def solution(distance, rocks, n):
    answer = 0
    if len(rocks)==n:
        return distance
    s, e = 0, distance
    rocks.sort()
    rocks = [0]+rocks+[distance]
    while s<e-1:
        mid = (s+e) // 2
        needRemove = 0
        index = 0
        nextIndex = 1
        while nextIndex<len(rocks):
            if rocks[nextIndex] - rocks[index] < mid:
                needRemove += 1
                nextIndex += 1
            else:
                nextIndex += 1
                index = nextIndex-1
        if needRemove>n:
            e = mid
        else:
            s = mid
    answer = (s+e)//2
    return answer