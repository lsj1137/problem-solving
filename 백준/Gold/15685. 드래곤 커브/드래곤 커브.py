# 반복문
# 한 세대가 끝나면 현재까지 모든 세대를 거꾸로 되돌아가면서 반시계방향으로 돌려서 추가

dir = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dots = [[0 for _ in range(102)] for _ in range(102)]

for _ in range(int(input())):
    x,y,d,g = map(int,input().split(' '))
    dots[x][y] = 1
    nextX = x+dir[d][0]
    nextY = y+dir[d][1]
    lines = [[nextX, nextY, d]]
    x,y = nextX, nextY
    dots[x][y] = 1
    while g > -1:
        maxInd = len(lines)-1
        for i in range(maxInd, -1, -1):
            line = lines[i]
            dirIndex = (line[2]+1) % 4
            nextX = x+dir[dirIndex][0]
            nextY = y+dir[dirIndex][1]
            lines.append([nextX, nextY, dirIndex])
            x,y = nextX, nextY
        if g==1:
            for l in lines:
                dots[l[0]][l[1]] = 1
        g -= 1

answer = 0
for i in range(102):
    for j in range(102):
        if dots[i][j]==1 and dots[i+1][j]==1 and dots[i][j+1]==1 and dots[i+1][j+1]==1:
            answer+=1
print(answer)