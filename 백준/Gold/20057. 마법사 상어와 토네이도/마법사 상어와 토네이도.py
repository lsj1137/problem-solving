import math

# 좌, 하, 우, 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dx001a = [-1, -1, 1, 1]
dy001a = [1, -1, -1, 1]
dx001b = [1, -1, -1, 1]
dy001b = [1, 1, -1, -1]
dx002a = [-2, 0, 2, 0]
dy002a = [0, -2, 0, 2]
dx002b = [2, 0, -2, 0]
dy002b = [0, 2, 0, -2]
dx005 = [0, 2, 0, -2]
dy005 = [-2, 0, 2 ,0]
dx007a = [-1, 0, 1, 0]
dy007a = [0, -1, 0, 1]
dx007b = [1, 0, -1, 0]
dy007b = [0, 1, 0, -1]
dx010a = [-1, 1, 1, -1]
dy010a = [-1, -1, 1, 1] 
dx010b = [1, 1, -1, -1]
dy010b = [-1, 1, 1, -1]
dxa = dx
dya = dy
curDir = 0 # 현재 방향
dirChanged = 0 # 방향 바뀐 횟수
maxMove = 1 # 직선 길이
move = 0 # 현재 직선에서 움직인 거리
result = 0 # 밖으로 나간 모래


def spread(sandBox, x, y, curDir):
    global result
    total = sandBox[x][y]
    sandBox[x][y] = 0
    t001 = math.floor(total*0.01)
    t002 = math.floor(total*0.02)
    t005 = math.floor(total*0.05)
    t007 = math.floor(total*0.07)
    t010 = math.floor(total*0.1)
    ta = total - t001*2 - t002*2 - t005 - t007*2 - t010*2
    
    dxList = [dx001a, dx001b, dx002a, dx002b, dx005, dx007a, dx007b, dx010a, dx010b, dxa]
    dyList = [dy001a, dy001b, dy002a, dy002b, dy005, dy007a, dy007b, dy010a, dy010b, dya]
    tList = [t001, t001, t002, t002, t005, t007, t007, t010, t010, ta]

    for i in range(len(dxList)):
        if x+dxList[i][curDir]>-1 and x+dxList[i][curDir]<len(sandBox) and y+dyList[i][curDir]>-1 and y+dyList[i][curDir]<len(sandBox):
            sandBox[x+dxList[i][curDir]][y+dyList[i][curDir]] += tList[i]
        else:
            result += tList[i]
    
    return sandBox

N = int(input())
x,y = N//2, N//2 # 시작은 가운데
sandBox = []
for _ in range(N):
    sandBox.append(list(map(int, input().split(' ')))) # 모래밭 초기화
while x!=0 or y!=0:
    x += dx[curDir]
    y += dy[curDir]
    move += 1
    sandBox = spread(sandBox, x, y, curDir)
    if move==maxMove: # 한 직선의 끝까지 움직이면 방향 전환
        curDir = (curDir+1) % 4
        dirChanged += 1
        move = 0
    if dirChanged==2: # 방향 전환 두 번 하면 길이 늘림
        maxMove += 1
        dirChanged = 0

print(result)