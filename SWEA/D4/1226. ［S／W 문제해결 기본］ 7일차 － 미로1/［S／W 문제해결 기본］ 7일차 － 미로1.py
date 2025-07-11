dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(16)]
    s, e = (0,0), (15,15)
    checked = [[False]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                s = (i,j)
            elif maze[i][j] == '3':
                e = (i,j)
            elif maze[i][j] == '1':
                checked[i][j] = True
    que = [s]
    newQue = []
    answer = 0
    while len(que)>0:
        cx,cy = que.pop()
        checked[cx][cy] = True
        if cx == e[0] and cy == e[1]:
            answer = 1
            break
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx>-1 and nx<16 and ny>-1 and ny<16 and not checked[nx][ny]:
                newQue.append((nx,ny))
        if len(que)==0:
            que = newQue
            newQue = []
    print(f'#{N} {answer}')