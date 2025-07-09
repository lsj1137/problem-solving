def checkPel(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(100)]
    answer = 1
    for i in range(100):
        for j in range(100):
            k = 99
            while k>answer:
                if board[i][j] == board[i][k]:
                    s = board[i][j:k+1]
                    if checkPel(s):
                        answer = max(answer, k-j+1)
                if board[j][i] == board[k][i]:
                    s = [board[r][i] for r in range(j,k+1)]
                    if checkPel(s):
                        answer = max(answer, k-j+1)
                k -= 1
    print(f'#{N} {answer}')