def check(board, x, y):
    ltr = True
    rtl = True
    for i in range(5):
        h = True
        v = True
        for j in range(5):
            if board[x+i][y+j] != 'o':
                h = False
            if board[x+j][y+i] != 'o':
                v = False
        if board[x+i][y+i] != 'o':
            ltr = False
        if board[x+i][y+4-i] != 'o':
            rtl = False
        if h or v:
            return True
    if ltr or rtl:
        return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    answer = 'NO'
    for i in range(0, N-4):
        for j in range(0, N-4):
            if check(board, i, j):
                answer = 'YES'
                break
    print(f'#{test_case} {answer}')