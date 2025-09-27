# 소요시간 02:20:46
from collections import deque

dxy = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]

class Tower():
    def __init__(self, x, y, power):
        self.x, self.y = x, y
        self.power = power
        self.recentAttack = -1
        self.relevant = False

    def __str__(self):
        return f'T[{self.x},{self.y}]:p={self.power} ra={self.recentAttack} |'

    def empower(self):
        self.power += N+M
        return

    def laser(self, time, defender):
        self.recentAttack = time
        self.relevant = True
        cx, cy = self.x, self.y
        atkPower = self.power
        curDist = distArr[cx][cy]
        while cx!=defender.x or cy!=defender.y:
            for i in range(0,8,2):
                dx, dy = dxy[i]
                nx, ny = cx+dx, cy+dy
                if not is_in(nx, ny):
                    nx, ny = to_opposite(nx, ny)
                if distArr[nx][ny]<curDist:
                    curDist = distArr[nx][ny]
                    tx, ty = nx, ny
            cx, cy = tx, ty
            if cx==defender.x and cy==defender.y:
                board[cx][cy].power -= atkPower
            else:
                board[cx][cy].power -= atkPower//2
            board[cx][cy].relevant = True
        return

    def bullet(self, time, defender):
        self.recentAttack = time
        self.relevant = True
        atkPower = self.power
        cx, cy = defender.x, defender.y
        board[cx][cy].power -= atkPower
        board[cx][cy].relevant = True
        for dx, dy in dxy:
            nx, ny = cx+dx, cy+dy
            if not is_in(nx, ny):
                nx, ny = to_opposite(nx, ny)
            if not board[nx][ny].isDead() and (nx!=self.x or ny!=self.y):
                board[nx][ny].power -= atkPower//2
                board[nx][ny].relevant = True
        return

    def isDead(self):
        return self.power<=0

    def fix(self):
        if not self.relevant:
            self.power += 1
        return

def is_in(x,y):
    return -1<x<N and -1<y<M

def to_opposite(x,y):
    return [(x+N)%N, (y+M)%M]

def findAttacker():
    tempTowers = [t for t in towers if not t.isDead()]
    tempTowers.sort(key=lambda t: (t.power, -t.recentAttack, -(t.x+t.y), -t.y))
    # print(*tempTowers)
    return tempTowers[0]

def findDefender():
    tempTowers = [t for t in towers if not t.isDead()]
    tempTowers.sort(key=lambda t: (-t.power, t.recentAttack, t.x+t.y, t.y))
    return tempTowers[0]

def searchPath(atk, dfd):
    global distArr
    distArr = [[float('inf')]*M for _ in range(N)]
    checked = [[False]*M for _ in range(N)]
    fromX, fromY = atk.x, atk.y
    toX, toY = dfd.x, dfd.y
    que = deque([[toX, toY, 0]])
    checked[toX][toY] = True
    while len(que)>0:
        cx, cy, dist = que.popleft()
        distArr[cx][cy] = dist
        if cx==fromX and cy==fromY:
            break
        for i in range(0,8,2):
            dx, dy = dxy[i]
            nx, ny = cx+dx, cy+dy
            if not is_in(nx,ny):
                nx, ny = to_opposite(nx, ny)
            if not checked[nx][ny] and not board[nx][ny].isDead():
                checked[nx][ny] = True
                que.append([nx,ny,dist+1])
    # print(distArr)
    return distArr[fromX][fromY]

def healingTime():
    alive = 0
    for t in towers:
        if not t.isDead():
            alive += 1
            t.fix()
        t.relevant = False
    return alive

N, M, K = map(int,input().split())
board = []
towers = []
distArr = [[float('inf')]*M for _ in range(N)]
for i in range(N):
    line = list(map(int,input().split()))
    towerLine = []
    for j in range(M):
        newTower = Tower(i,j,line[j])
        towerLine.append(newTower)
        towers.append(newTower)
    board.append(towerLine)


for k in range(K):
    atk = findAttacker()
    dfd = findDefender()
    atk.empower()
    if searchPath(atk, dfd)!=float('inf'):
        atk.laser(k,dfd)
    else:
        atk.bullet(k,dfd)
    # print(*towers)
    alive = healingTime()
    if alive == 1:
        break

print(findDefender().power)
