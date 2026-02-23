import sys
import heapq
input = sys.stdin.readline

N = int(input())
max_q = []
for i in range(N):
    nl = list(map(int, input().split()))
    if i==0:
        heapq.heapify(nl)
        max_q = nl
    else:
        for n in nl:
            if n>max_q[0]:
                heapq.heappop(max_q)
                heapq.heappush(max_q, n)
print(max_q[0])