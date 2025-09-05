from collections import deque

nxys = [
  [(-1,1), (0,1), (1,1)],
  [(-1,-1), (0,-1), (1,-1)],
  [(-1,-1), (-1,0), (-1,1)],
  [(1,-1), (1,0), (1,1)],
]

class Heater:
  def __init__(self, x, y, d):
    self.x, self.y, self.d = x, y, d
    self.heatMap = [[0 for _ in range(C)] for _ in range(R)]

  def setHeatMap(self):
    dxy = [(0,1), (0,-1), (-1,0), (1,0)]
    sdx, sdy = dxy[self.d]
    startX = self.x + sdx
    startY = self.y + sdy
    heat = 5
    que = deque([(startX, startY, heat)])
    nxy = nxys[self.d]
    while len(que)>0:
      cx, cy, ch = que.popleft()
      if ch<1:
        continue
      self.heatMap[cx][cy] = ch
      for i in range(3):
        dx, dy = nxy[i]
        nx, ny = cx + dx, cy + dy
        if isInRoom(nx,ny) and canGo(cx, cy, nx, ny, self.d):
            que.append((nx, ny, ch-1))
    return

  def blowWind(self):
    for i in range(R):
      for j in range(C):
        room[i][j]+=self.heatMap[i][j]
    return
  
  
  
def isInRoom(x,y):
  return -1<x<R and -1<y<C

def canGo(cx,cy,nx,ny,d):
  if cx==nx or cy==ny:
    return walls[cx][cy][d]==0
  else:
    if d==0 or d==1:
      if nx>cx:
        return walls[cx][cy][3]==0 and walls[cx+1][cy][d]==0
      elif nx<cx:
        return walls[cx][cy][2]==0 and walls[cx-1][cy][d]==0
    else:
      if ny>cy:
        return walls[cx][cy][0]==0 and walls[cx][cy+1][d]==0
      elif ny<cy:
        return walls[cx][cy][1]==0 and walls[cx][cy-1][d]==0

def activateHeater():
  for heater in heaters:
    heater.blowWind()
  return

def heatSpread():
  global room
  dxy = [(0, 1), (0, -1), (-1,0), (1, 0)]
  newRoom = [r[:] for r in room]
  checked = [[False]*C for _ in range(R)]
  for i in range(R):
    for j in range(C):
      for k in range(4):
        dx, dy = dxy[k]
        nx = i+dx
        ny = j+dy
        if isInRoom(nx,ny) and not checked[nx][ny] and canGo(i,j,nx,ny,k) and abs(room[nx][ny]-room[i][j])>=4:
          dt = abs(room[nx][ny]-room[i][j])//4
          if room[nx][ny]>room[i][j]:
            newRoom[nx][ny] -= dt
            newRoom[i][j] += dt
          else:
            newRoom[nx][ny] += dt
            newRoom[i][j] -= dt        
      checked[i][j] = True
  room = newRoom
  return

def heatLoss():
  global room
  for i in range(R):
    for j in range(C):
      if j==0 or j==C-1 or i==0 or i==R-1:
        if room[i][j]>0:
          room[i][j] -=1
  return

def isFinish():
  for x, y in target:
    if room[x][y]<K:
      return False
  return True

R, C, K = map(int, input().split())
room = [list(map(int,input().split())) for _ in range(R)]
heaters = []
walls = [[[0,0,0,0] for _ in range(C)] for _ in range(R)]
target = []
W = int(input())
for _ in range(W):
  x,y,t = map(int, input().split())
  if t==0:
    walls[x-1][y-1][2] = 1
    walls[x-2][y-1][3] = 1
  else:
    walls[x-1][y-1][0] = 1
    walls[x-1][y][1] = 1

for i in range(R):
  for j in range(C):
    if room[i][j]==0:
      continue
    elif room[i][j]==5:
      target.append((i,j))
    else:
      heaters.append(Heater(i,j,room[i][j]-1))
    room[i][j] = 0

for heater in heaters:
  heater.setHeatMap()

answer = 0
while answer<101:
  #1
  activateHeater()
#   print('ah---')
#   for r in room:
#       print(r)
  #2
  heatSpread()
#   print('hs---')
#   for r in room:
#       print(r)
  #3
  heatLoss()
#   print('hl---')
#   for r in room:
#     print(r)
  #4
  answer += 1
  #5
  if isFinish():
    break
print(answer)