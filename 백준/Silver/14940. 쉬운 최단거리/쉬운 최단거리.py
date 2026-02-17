from collections import deque

dxy = [[-1,0], [0,1], [1,0], [0,-1]]

N, M = map(int, input().split())
world_map = [list(map(int, input().split())) for _ in range(N)]
result_map = [[-1 for _ in range(M)] for _ in range(N)]

checked = [[False for _ in range(M)] for _ in range(N)]
sx, sy = 0, 0
for i in range(N):
    for j in range(M):
        if world_map[i][j] == 0:
            checked[i][j] = True
            result_map[i][j] = 0
        if world_map[i][j] == 2:
            sx, sy = i, j

que = deque([[sx, sy, 0]])
while len(que)>0:
    cx, cy, dist = que.popleft()
    result_map[cx][cy] = dist
    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        if -1<nx<N and -1<ny<M and not checked[nx][ny] and world_map[nx][ny]==1:
            checked[nx][ny] = True
            que.append([nx,ny,dist+1])

for road in result_map:
    print(*road)