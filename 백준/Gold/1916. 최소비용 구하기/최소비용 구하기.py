import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
cost = [[float('inf')]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s,e,c = map(int, input().split())
    cost[s][e] = min(cost[s][e], c)
s,e = map(int,input().split())

que = deque([])
for i in range(N+1):
    cost[i][i] = 0
    if cost[s][i]!=float('inf'):
        que.append(i)

while len(que)>0:
    next_dest = que.popleft()
    for i in range(N+1):
        if cost[s][i] > cost[s][next_dest] + cost[next_dest][i]:
            cost[s][i] = cost[s][next_dest] + cost[next_dest][i]
            que.append(i)

print(cost[s][e])