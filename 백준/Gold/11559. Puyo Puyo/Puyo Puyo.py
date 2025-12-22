dxy = [(-1,0), (0,1), (1,0), (0,-1)]

field = list(list(input()) for _ in range(12))

combo = 0
while True:
    checked = [[False] *6 for _ in range(12)]
    keepGoing = False
    for i in range(12):
        for j in range(6):
            if field[i][j]!='.' and not checked[i][j]:
                que = [[i,j]]
                group = []
                size = 0
                checked[i][j] = True
                while len(que)>0:
                    cx,cy = que.pop()
                    c_col = field[cx][cy]
                    group.append([cx,cy])
                    size += 1
                    for dx,dy in dxy:
                        nx, ny = cx+dx, cy+dy
                        if -1<nx<12 and -1<ny<6 and not checked[nx][ny] and field[nx][ny]==c_col:
                            checked[nx][ny] = True
                            que.append([nx, ny])
                if size>3:
                    keepGoing = True
                    for x,y in group:
                        field[x][y] = '.'
    for i in range(11,-1,-1):
        for j in range(0,6):
            if field[i][j]!='.':
                cx = i
                while cx+1<12 and field[cx+1][j]=='.':
                    field[cx+1][j] = field[cx][j]
                    field[cx][j] = '.'
                    cx += 1
    if keepGoing:
        combo += 1
    else:
        break
print(combo)