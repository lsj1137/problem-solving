import sys
import heapq
input = sys.stdin.readline

N = int(input())
max_q = []
for i in range(N):
    nl = list(map(lambda x:(-int(x), int(x)), input().split()))
    heapq.heapify(nl)
    if i==0:
        max_q = [x[1] for x in nl]
    else:
        while max_q[0]<nl[0][1]:
            a = heapq.heappop(nl)
            b = heapq.heappop(max_q)
            heapq.heappush(nl, (-b,b))
            heapq.heappush(max_q, a[1])
print(max_q[0])