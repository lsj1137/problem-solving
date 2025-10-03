from collections import deque

dxy = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def fillArea(field, rectangle):
    lx, ly, rx, ry = rectangle
    for i in range(ly*3, ry*3+1):
        for j in range(lx*3, rx*3+1):
            field[i][j] = 1
    return

def canGo(field,x,y):
    if field[y][x]==0:
        return False
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if field[ny][nx]==0:
            return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[0]*156 for _ in range(156)]
    for rec in rectangle:
        fillArea(field, rec)
        
    checked = [[False]*156 for _ in range(156)]
    checked[characterY*3][characterX*3] = True
    que = deque([[characterX*3, characterY*3,0]])
    while len(que)>0:
        cx, cy, dist = que.popleft()
        # print(cx//3,cy//3, dist)
        if cx==itemX*3 and cy==itemY*3:
            answer = dist
            break
        for i in range(0,8,2):
            dx, dy = dxy[i]
            nx, ny = cx+dx*3, cy+dy*3
            if canGo(field,cx+dx,cy+dy) and not checked[ny][nx]:
                checked[ny][nx] = True
                que.append([nx,ny,dist+1])
    
    return answer