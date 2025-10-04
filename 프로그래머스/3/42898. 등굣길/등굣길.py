# from collections import deque

def dp(board, sx, sy, ex, ey):
    if sx==ex and sy==ey:
        return 1
    result = 0
    if sx+1<=ex and board[sx+1][sy]>=0:
        if board[sx+1][sy]==0:
            board[sx+1][sy] = dp(board, sx+1, sy, ex, ey)
        result += board[sx+1][sy]
    if sy+1<=ey and board[sx][sy+1]>=0:
        if board[sx][sy+1]==0:
            board[sx][sy+1] = dp(board, sx, sy+1, ex, ey)
        result += board[sx][sy+1]
    return result%1000000007
    

def solution(m, n, puddles):
    answer = 0
    board = [[0]*m for _ in range(n)]
    for x,y in puddles:
        board[y-1][x-1] = -1
    answer = dp(board, 0, 0, n-1, m-1)
    return answer