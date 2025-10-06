import heapq

def solution(n, works):
    answer = 0
    works = list(map(lambda x:(-x,x),works))
    heapq.heapify(works)
    while n>0:
        index, biggest = heapq.heappop(works)
        if biggest>0:
            index += 1
            biggest -= 1
        n -= 1
        heapq.heappush(works, (index, biggest))
    # print(works)
    answer = sum(map(lambda x:x**2, [w[1] for w in works]))
    return answer