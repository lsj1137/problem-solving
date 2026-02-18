from collections import deque

dxy = [[-1,0], [0,1], [1,0], [0,-1]]

N,M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
checked = [[False]*M for _ in range(N)]
sx, sy = 0, 0 
for i in range(N):
    for j in range(M):
        if campus[i][j] =='I':
            sx, sy = i, j
            checked[i][j] = True

result = 0
que = deque([[sx,sy]])
while len(que)>0:
    cx, cy = que.popleft()
    if campus[cx][cy] == 'P':
        result += 1
    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        if -1 < nx < N and -1 < ny < M and not checked[nx][ny] and campus[nx][ny] != 'X':
            checked[nx][ny] = True
            que.append([nx,ny])

if result==0:
    result = 'TT'
print(result)