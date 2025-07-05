dx = [-1,0,1,0]
dy = [0,1,0,-1]

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    road = [list(map(int, list(input()))) for _ in range(N)]
    work = [[float('inf')]*N for _ in range(N)]
    work[0][0] = 0
    que = [[0,0]]
    newQue = []
    while len(que)>0:
        x,y = que.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>-1 and nx<N and ny>-1 and ny<N:
                if work[nx][ny] > work[x][y] + road[nx][ny]:
                    work[nx][ny] = work[x][y] + road[nx][ny]
                    newQue.append([nx,ny])
        if len(que) == 0:
            que = newQue
            newQue = []
    result = work[N-1][N-1]
    print(f'#{test_case} {result}')