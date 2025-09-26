# 소요시간 01:34:33
from collections import deque

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

# 조건에 따라 격자 선택
def choose3x3():
    candidates = []
    for i in range(1,4):
        for j in range(1,4):
            newPlace = [p[:] for p in place]
            for k in range(3):
                rotatedPlace = rotate(i,j,newPlace)
                value, spots = searchParts(rotatedPlace)
                candidates.append([value,k+1,j,i])
                newPlace = rotatedPlace
    # 회전 우선순위 - 획득가치(내)>회전수(오)>열번호(오)>행번호(오)
    candidates.sort(key=lambda x:(-x[0],x[1],x[2],x[3]))
    # print(candidates)
    return candidates[0]

# 선택된 격자 회전하고 유물 획득
def makeProduct(x,y,r):
    global place
    for _ in range(r):
        place = rotate(x, y, place)
    totalValue = 0
    while True:
        value, spots = searchParts(place)
        if value==0:
            break
        totalValue += value
        spots.sort(key=lambda x: (x[1], -x[0]))
        # 빈곳 채우기
        for nx, ny in spots:
            place[nx][ny] = refill.popleft()
    return totalValue

# 회전 (시계:90)
def rotate(cx, cy, place):
    temp = [p[:] for p in place]
    temp[cx-1][cy-1] = place[cx+1][cy-1]
    temp[cx-1][cy] = place[cx][cy-1]
    temp[cx-1][cy+1] = place[cx-1][cy-1]
    temp[cx][cy-1] = place[cx+1][cy]
    temp[cx][cy+1] = place[cx-1][cy]
    temp[cx+1][cy-1] = place[cx+1][cy+1]
    temp[cx+1][cy] = place[cx][cy+1]
    temp[cx+1][cy+1] = place[cx-1][cy+1]
    return temp

# 연결 조각들의 가치합 & 위치 확인
def searchParts(rotatedPlace):
    checked = [[False]*5 for _ in range(5)]
    value = 0
    linkedSpots = []
    for i in range(5):
        for j in range(5):
            if checked[i][j]:
                continue
            checked[i][j] = True
            spots = dfs(i,j,rotatedPlace,checked)
            if len(spots)>=3:
                value += len(spots)
                linkedSpots += spots
    return [value, linkedSpots]

# 깊이우선탐색으로 붙어있는 조각 확인
def dfs(x,y,place,checked):
    num = place[x][y]
    spots = [(x,y)]
    que = [[x,y]]
    checked[x][y] = True
    while len(que)>0:
        cx, cy = que.pop()
        for dx, dy in dxy:
            nx, ny = cx+dx, cy+dy
            if is_in(nx, ny) and not checked[nx][ny] and place[nx][ny]==num:
                checked[nx][ny] = True
                que.append([nx,ny])
                spots.append((nx,ny))
    return spots

def is_in(x,y):
    return -1<x<5 and -1<y<5

K, M = map(int, input().split())
place = [list(map(int,input().split()))for _ in range(5)]
refill = deque(list(map(int,input().split())))
result = []
for k in range(K):
    gain = 0
    # 격자 선택
    v, r, y, x = choose3x3()
    # 유물 획득
    gain += makeProduct(x,y,r)
    if gain==0:
        break
    else:
        result.append(gain)
print(*result)
