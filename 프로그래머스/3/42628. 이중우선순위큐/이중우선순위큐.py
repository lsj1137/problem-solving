from collections import deque
import heapq
def solution(operations):
    answer = []
    minq = []
    maxq = []
    for o in operations:
        org = list(o.split())
        if org[0] == 'I':
            n = int(org[1])
            heapq.heappush(minq,n)
            heapq.heappush(maxq,(-n,n))
        else:
            if not minq:
                continue
            if org[1] == '1':
                x = heapq.heappop(maxq)
                minq.remove(-x[0])
            else:
                x = heapq.heappop(minq)
                maxq.remove((-x,x))
    if minq:
        answer.append(maxq[0][1])
        answer.append(minq[0])
    else:
        answer = [0,0]
    return answer