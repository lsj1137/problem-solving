dx = [-1, 0 ,1, 0]
dy = [0, 1, 0, -1]

def copyRoom(room):
    newRoom = []
    for i in range(R):
        row = []
        for j in range(C):
            row.append(room[i][j])
        newRoom.append(row)
    return newRoom

def diffusion(room):
    newRoom = copyRoom(room)
    for i in range(R):
        for j in range(C):
            if room[i][j]<1: continue
            dust = room[i][j]//5
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if nx>-1 and nx<R and ny>-1 and ny<C and room[nx][ny]!=-1:
                    newRoom[nx][ny] += dust
                    newRoom[i][j] -= dust
    return newRoom

def clean(room, cleaner):
    a = cleaner[0]
    b = cleaner[1]
    newRoom = copyRoom(room)
    newRoom[a][1], newRoom[b][1] = 0, 0
    for x in range(1, C-1):
        newRoom[a][x+1] = room[a][x]
    for y in range(a, 0, -1):
        newRoom[y-1][C-1] = room[y][C-1]
    for x in range(C-1, 0, -1):
        newRoom[0][x-1] = room[0][x]
    for y in range(a-1):
        newRoom[y+1][0] = room[y][0]
    for x in range(1, C-1):
        newRoom[b][x+1] = room[b][x]
    for y in range(b, R-1):
        newRoom[y+1][C-1] = room[y][C-1]
    for x in range(C-1, 0, -1):
        newRoom[R-1][x-1] = room[R-1][x]
    for y in range(R-1, b+1, -1):
        newRoom[y-1][0] = room[y][0]
    return newRoom

R, C, T = map(int, input().split())
room = []
cleaner = []
for i in range(R):
    room.append(list(map(int,input().split())))
    if room[-1][0] == -1:
        cleaner.append(i)

for _ in range(T):
    diffuseRoom = diffusion(room)
    cleanRoom = clean(diffuseRoom, cleaner)
    room = cleanRoom

result = 2
for i in range(R):
    result += sum(room[i])
print(result)