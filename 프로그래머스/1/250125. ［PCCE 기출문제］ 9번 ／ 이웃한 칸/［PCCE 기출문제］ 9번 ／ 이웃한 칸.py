def solution(board, h, w):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if nx>-1 and nx<len(board) and ny>-1 and ny<len(board[0]) and board[nx][ny]==board[h][w]:
            answer+=1
    return answer