dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗

def moveFish(situation):
    position = {}
    for i in range(4):
        for j in range(4):
            position[situation[i][j][0]] = [i, j]
    for i in range(1, 17):
        if i in position:
            x = position[i][0]
            y = position[i][1]
            for j in range(8):
                d = (situation[x][y][1]-1+j) % 8
                nx = x+dx[d]
                ny = y+dy[d]
                if nx>-1 and nx<4 and ny>-1 and ny<4 and situation[nx][ny][0] != -1:
                    situation[x][y][1] = d+1
                    origin = i
                    dest = situation[nx][ny][0]
                    temp = [situation[x][y][0], situation[x][y][1]]
                    situation[x][y] = [situation[nx][ny][0], situation[nx][ny][1]]
                    situation[nx][ny] = temp
                    temp2 = [position[origin][0], position[origin][1]]
                    position[origin] = [position[dest][0], position[dest][1]]
                    position[dest] = temp2
                    break
    return situation

def moveShark(situation):
    newSituations = []
    sharkX, sharkY = 0,0
    sharkD = 0
    for i in range(4):
        for j in range(4):
            if situation[i][j][0] == -1:
                sharkX, sharkY = i, j
                sharkD = situation[i][j][1] - 1
    nx = sharkX + dx[sharkD]
    ny = sharkY + dy[sharkD]
    while nx>-1 and nx<4 and ny>-1 and ny<4:
        if situation[nx][ny][0] > 0:
            newSituation = copySpace(situation)
            newSituation[sharkX][sharkY][0] = 0
            newSituation[nx][ny][0] = -1
            newSituations.append(newSituation)
        nx += dx[sharkD]
        ny += dy[sharkD]
    return newSituations

def calRemainFish(space):
    result = 0
    for i in range(4):
        for j in range(4):
            result += space[i][j][0]
    return result

def copySpace(space):
    newSpace = []
    for i in range(4):
        spaceRow = []
        for j in range(4):
            spaceRow.append([space[i][j][0],space[i][j][1]])
        newSpace.append(spaceRow)
    return newSpace

space = []

for _ in range(4):
    a, da, b, db, c, dc, d, dd = map(int,input().split())
    space.append([[a,da], [b,db], [c,dc], [d,dd]])

initialFishes = calRemainFish(space)
space[0][0][0] = -1 #상어
situations = [space]
result = 0
while len(situations)>0:
    situation = situations.pop()
    result = max(result, initialFishes-calRemainFish(situation))
    situation = moveFish(situation) 
    newSituations = moveShark(situation)
    for s in newSituations:
        situations.append(s)
print(result-1)