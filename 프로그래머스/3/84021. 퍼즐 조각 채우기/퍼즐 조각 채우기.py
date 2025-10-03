from collections import deque

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def getBlocks(N, table, isTable):
    blocks = []
    checked = [[False]*N for _ in range(N)]
    condition = 1 if isTable else 0
    for i in range(N):
        for j in range(N):
            if checked[i][j] or table[i][j]==1-condition:
                continue
            checked[i][j] = True
            que = deque([(i,j)])
            newBlock = [(i,j)]
            while len(que)>0:
                cx, cy = que.popleft()
                for dx, dy in dxy:
                    nx, ny = cx+dx, cy+dy
                    if -1<nx<N and -1<ny<N and not checked[nx][ny] and table[nx][ny]==condition:
                        checked[nx][ny] = True
                        que.append((nx,ny))
                        newBlock.append((nx,ny))
            blocks.append(newBlock)
    return blocks

def rotate(N,block):
    rotatedBlock = []
    for sp in block:
        rotatedBlock.append((sp[1], N-1-sp[0]))
    return rotatedBlock

def moveToZero(block):
    minX, minY = float('inf'), float('inf')
    for x,y in block:
        minX = min(minX,x)
        minY = min(minY,y)
    newBlock = []
    for x,y in block:
        newBlock.append((x-minX, y-minY))
    return newBlock

def checkFit(checked, block):
    for x,y in block:
        if not checked[x][y]:
            return False
    return True

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    
    blocks = []
    originBlocks = getBlocks(N, table, True)
    for block in originBlocks:
        blockSet = [moveToZero(block)]
        for i in range(3):
            block = rotate(N, block)
            blockSet.append(moveToZero(block))
        blocks.append(blockSet)
    
    checkUsedBlock = [False]*len(blocks)
    blanks = getBlocks(N, game_board, False)
    for blank in blanks:
        checked = [[False]*N for _ in range(N)]
        movedBlank = moveToZero(blank)
        # print(movedBlank)
        for x,y in movedBlank:
            checked[x][y] = True
        for i, blockSet in enumerate(blocks):
            if checkUsedBlock[i]:
                continue
            if len(blockSet[0])!=len(blank):
                continue
            for block in blockSet:
                if checkFit(checked, block):
                    answer += len(blank)
                    # print(blank, block)
                    checkUsedBlock[i] = True
                    break
            if checkUsedBlock[i]:
                break
        
    return answer