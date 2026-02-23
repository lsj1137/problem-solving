import sys
import math
import heapq

input = sys.stdin.readline

for _ in range(int(input())):
    M = int(input())
    arr = []
    for _ in range(math.ceil(M/10)):
        arr += list(map(int,input().split()))

    max_heap = []
    min_heap = []
    middles = [[]]
    total = 0
    for i in range(M):
        heapq.heappush(max_heap, (-arr[i], arr[i]))
        heapq.heappush(min_heap, arr[i])
        if i%2==0:
            while max_heap[0][1]!=min_heap[0]:
                maxx = heapq.heappop(max_heap)
                minn = heapq.heappop(min_heap)
                heapq.heappush(min_heap, maxx[1])
                heapq.heappush(max_heap, (-minn, minn))
            total += 1
            if len(middles[-1])<10:
                middles[-1].append(min_heap[0])
            else:
                middles.append([min_heap[0]])
    print(total)
    for middle in middles:
        print(*middle)