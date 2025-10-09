def solution(n, times):
    answer = 0
    times.sort()
    shortest, longest = times[0], times[0]*n
    while True:
        mid = (shortest+longest) // 2
        count = 0
        for t in times:
            count += mid//t
        if count>=n:
            longest = mid
        else:
            shortest = mid
        if shortest==longest-1:
            break
    answer = longest
    return answer