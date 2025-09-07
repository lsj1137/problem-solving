from collections import deque

dxy = [(-1,0),(0,1),(1,0),(0,-1)]

class Robot:
    def __init__(self, x, y, level):
        self.x, self.y, self.level = x,y,level
        self.killCount = 0

    def kill(self):
        self.killCount += 1
        if self.killCount == self.level:
            self.level += 1
            self.killCount = 0
        return

    def findRoute(self, monster):
        mx, my = monster.x, monster.y
        return result

    def moveTo(self, x, y):
        self.x, self.y = x, y
        return

    def refreshDist(self):
        global distArr
        distArr = [[float('inf') for _ in range(n)] for _ in range(n)]
        checked = [[False]*n for _ in range(n)]
        que = deque([(self.x, self.y, 0)])
        checked[self.x][self.y] = True
        while len(que)>0:
            cx,cy,moved = que.popleft()
            distArr[cx][cy] = moved
            for i in range(4):
                dx, dy = dxy[i]
                nx = cx + dx
                ny = cy + dy
                if isIn(nx,ny) and not checked[nx][ny] and self.level>=space[nx][ny]:
                    checked[nx][ny] = True
                    que.append((nx,ny, moved+1))
        applyDist()
        return


class Monster:
    def __init__(self, x, y, level):
        self.x, self.y, self.level = x,y,level
        self.dist = 0

    def __str__(self):
        return f'M:level={self.level} x={self.x} y={self.y} d={self.dist} //'

def isIn(x,y):
    return -1<x<n and -1<y<n


def applyDist():
    for m in monsters:
        m.dist = distArr[m.x][m.y]
    monsters.sort(key=lambda m:(m.dist, m.x, m.y))
    return

n = int(input())
space = [list(map(int,input().split())) for _ in range(n)]
robot = None
monsters = []
distArr = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if space[i][j]==0:
            continue
        elif space[i][j]==9:
            robot = Robot(i,j,2)
            space[i][j] = 0
        else:
            monsters.append(Monster(i,j,space[i][j]))
robot.refreshDist()

answer = 0
while True:
    keepGoing = False
    for m in monsters:
        if m.level>=robot.level or m.dist==float('inf'):
            continue
        # print(m)
        keepGoing = True
        answer += m.dist
        robot.moveTo(m.x, m.y)
        robot.kill()
        monsters.remove(m)
        space[robot.x][robot.y] = 0
        robot.refreshDist()
        break
    if not keepGoing:
        break
print(answer)
