dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, board, depth, cur):
    result = set([])
    if depth == 7:
        return set([cur])
    cur += board[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>-1 and nx<4 and ny>-1 and ny<4:
            result = result.union(dfs(nx, ny, board, depth+1, cur))
    return result

T = int(input())
for test_case in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]
    possibles = set([])
    for i in range(4):
        for j in range(4):
            possibles = possibles.union(dfs(i,j,board,0,''))
    answer = len(possibles)
    print(f'#{test_case} {answer}')