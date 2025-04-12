greenBoard = [[0]*4 for _ in range(10)]
blueBoard = [[0]*4 for _ in range(10)]

def rotateRedBlock():
    newRed = []
    newRed.append([redBoard[i][0] for i in range(3,-1,-1)])
    newRed.append([redBoard[i][1] for i in range(3,-1,-1)])
    newRed.append([redBoard[i][2] for i in range(3,-1,-1)])
    newRed.append([redBoard[i][3] for i in range(3,-1,-1)])
    rotated = []
    for i in range(4):
        for j in range(4):
            if newRed[i][j] == 1:
                rotated.append([i,j])
    return rotated

def drop(block, board):
    moving = True
    while moving:
        for b in block:
            x = b[0]
            y = b[1]
            nx = x + 1
            if nx>len(board)-1 or board[nx][y]==1:
                moving = False
        if moving:
            for b in block:
                b[0] += 1
    for b in block:
        board[b[0]][b[1]] = 1

def eraseLine(board):
    global score
    for i in range(4, len(board)):
        if sum(board[i])==4:
            board[i] = [0,0,0,0]
            score += 1
    for i in range(4, len(board)):
        if sum(board[i])==0:
            for j in range(i, 3, -1):
                board[j] = [board[j-1][0], board[j-1][1], board[j-1][2], board[j-1][3]]
    return

def eraseSpecial(board):
    lineCount = 0
    if sum(board[5]) != 0:
        lineCount += 1
    if sum(board[4]) != 0:
        lineCount += 1
    for _ in range(lineCount):
        for j in range(9, 3, -1):
            board[j] = [board[j-1][0], board[j-1][1], board[j-1][2], board[j-1][3]]
    return

score = 0
for _ in range(int(input())):
    redBoard = [[0]*4 for _ in range(4)]
    t, x, y = map(int, input().split())
    origin = []
    if t==1:
        redBoard[x][y] = 1
        origin.append([x,y])
    elif t==2:
        redBoard[x][y] = 1
        redBoard[x][y+1] = 1
        origin.append([x,y])
        origin.append([x,y+1])
    elif t==3:
        redBoard[x][y] = 1
        redBoard[x+1][y] = 1
        origin.append([x,y])
        origin.append([x+1,y])
    rotated = rotateRedBlock()
    drop(origin, greenBoard)
    drop(rotated, blueBoard)
    eraseLine(greenBoard)
    eraseLine(blueBoard)
    eraseSpecial(greenBoard)
    eraseSpecial(blueBoard)
print(score)
remain = sum(sum(blueBoard[i]) for i in range(len(blueBoard))) + sum(sum(greenBoard[i]) for i in range(len(greenBoard)))
print(remain)