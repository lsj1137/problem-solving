# 원판을 덱으로 바꿔서 생각하기
# 인접한 칸을 dfs로 확인하고 같으면 0으로 바꿈
# 0으로 바꾼게 없으면 평균 구해서 +1/-1

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def removeSame(x,y,checked):
    searching = disks[x][y]
    checkPoint = [x,y]
    checkQue = [checkPoint]
    foundSame = False
    while len(checkQue)>0:
        checkPoint = checkQue.pop()
        checked[checkPoint[0]][checkPoint[1]] = True
        if foundSame:
            disks[checkPoint[0]][checkPoint[1]] = 0
        for i in range(4):
            nx = checkPoint[0]+dx[i]
            ny = checkPoint[1]+dy[i]
            if ny == -1:
                ny = M-1
            elif ny == M:
                ny = 0
            if nx>-1 and nx<N and not checked[nx][ny] and disks[nx][ny]==searching:
                checkQue.append([nx,ny])
                disks[checkPoint[0]][checkPoint[1]] = 0
                foundSame = True
    return [checked, foundSame]

N, M, T = map(int, input().split())
disks = []
for _ in range(N):
    disk = deque(map(int,input().split()))
    disks.append(disk)

for _ in range(T):
    x, d, k = map(int,input().split())
    for i in range(x-1, N, x):
        if d==0:
            for _ in range(k):
                disks[i].appendleft(disks[i].pop())
        else:
            for _ in range(k):
                disks[i].append(disks[i].popleft())

    checked = [[False for _ in range(M)] for _ in range(N)]
    foundSame = False
    for i in range(N):
        for j in range(M):
            if not checked[i][j] and disks[i][j]!=0:
                checked, changed = removeSame(i, j, checked)
                if changed:
                    foundSame = True

    if not foundSame:
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if disks[i][j] != 0:
                    count += 1
                    total += disks[i][j]
        if count==0:
            continue
        avg = total/count
        for i in range(N):
            for j in range(M):
                if disks[i][j] != 0:
                    if disks[i][j] > avg:
                        disks[i][j] -= 1
                    elif disks[i][j] < avg:
                        disks[i][j] += 1

answer = sum(sum(disks[i]) for i in range(N))
print(answer)