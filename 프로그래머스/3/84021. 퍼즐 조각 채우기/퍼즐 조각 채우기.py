from collections import deque

dxy = [(-1,0), (0,1), (1,0), (0,-1)]

# 주어진 배열을 탐색하며 모든 블럭(이어진 칸들)을 찾아 반환
# isTable이 True일때는 테이블을 탐색하는 것이고,
# False일때는 게임보드를 탐색하는 것임.
def getBlocks(N, table, isTable):
    blocks = []
    checked = [[False]*N for _ in range(N)]
    condition = 1 if isTable else 0
    # 모든 좌표
    for i in range(N):
        for j in range(N):
            if checked[i][j] or table[i][j]==1-condition:
                continue
            # 검사 안된 곳이라면 여기부터 검사
            # bfs
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

# N*N판 위에서 90도 회전
def rotate(N,block):
    rotatedBlock = []
    for sp in block:
        rotatedBlock.append((sp[1], N-1-sp[0]))
    return rotatedBlock

# 블록의 좌상단이 [0,0]에 맞도록 당겨오기
def moveToZero(block):
    minX, minY = float('inf'), float('inf')
    for x,y in block:
        minX = min(minX,x)
        minY = min(minY,y)
    newBlock = []
    for x,y in block:
        newBlock.append((x-minX, y-minY))
    return newBlock

# 구멍과 블록이 맞는지 확인
def checkFit(checked, block):
    for x,y in block:
        if not checked[x][y]:
            return False
    return True

def solution(game_board, table):
    answer = 0
    N = len(game_board)
    
    blocks = []
    # 테이블 돌면서 블록 탐색
    originBlocks = getBlocks(N, table, True)
    for block in originBlocks:
        # 블록셋 생성 (같은 블록셋안에 있다면 같은 블록을 회전만 시켰다는 뜻)
        blockSet = [moveToZero(block)]
        for i in range(3):
            # 블록 회전
            block = rotate(N, block)
            # 회전한 블록을 [0,0]에 맞추고 블록셋에 추가
            blockSet.append(moveToZero(block))
        # 블록 배열에 블록셋 추가
        blocks.append(blockSet)
    
    # 특정 블록이 구멍을 메꾸는데 이미 사용됐는지 확인용 Boolean 배열
    checkUsedBlock = [False]*len(blocks)
    # 게임보드 돌면서 구멍 탐색
    blanks = getBlocks(N, game_board, False)
    # 각 구멍마다 블록이 들어가는지 확인
    for blank in blanks:
        # 구멍과 블록이 맞는지 확인하는 용도의 Boolean 배열
        checked = [[False]*N for _ in range(N)]
        # 구멍을 [0,0] 좌표에 맞춤
        movedBlank = moveToZero(blank)
        # 구멍 위치를 checked에 표시
        for x,y in movedBlank:
            checked[x][y] = True
        # 블록 배열 순회하면서 확인
        for i, blockSet in enumerate(blocks):
            # 이미 사용된 블록이면 넘어감
            if checkUsedBlock[i]:
                continue
            # 블록 크기가 다르면 넘어감
            if len(blockSet[0])!=len(blank):
                continue
            # 블록을 회전하면서 맞춰보기 (=블록셋 안에 블록들 순회)
            for block in blockSet:
                # 블록의 좌표가 checked의 False에 해당되면 안맞는 것임
                if checkFit(checked, block):
                    # 메워진만큼(구멍크기) answer에 더하기
                    answer += len(blank)
                    # 사용된 블록임을 표시
                    checkUsedBlock[i] = True
                    break
            # 메꿔진 구멍이면 넘어감
            if checkUsedBlock[i]:
                break
        
    return answer