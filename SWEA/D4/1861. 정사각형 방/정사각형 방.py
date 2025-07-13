dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    checked = [[False]*N for _ in range(N)]
    start, amount = 0, 0
    for i in range(N):
        for j in range(N):
            if not checked[i][j]:
                que = [(i,j)]
                s, r = N**2, 0
                while len(que)>0:
                    x,y = que.pop()
                    checked[x][y] = True
                    r += 1
                    s = min(s, rooms[x][y])
                    for k in range(4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        if nx>-1 and nx<N and ny>-1 and ny<N and not checked[nx][ny] and abs(rooms[nx][ny]-rooms[x][y])==1:
                            que.append((nx,ny))
                if r>amount:
                    amount = r
                    start = s
                elif r==amount:
                    start = min(s,start)
    print(f'#{test_case} {start} {amount}')