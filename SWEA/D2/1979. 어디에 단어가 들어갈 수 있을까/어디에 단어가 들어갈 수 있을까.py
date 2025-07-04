T = int(input())
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    v, h = 0, 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                h += 1
            else:
                if h==K:
                    result += 1
                h = 0
            if puzzle[j][i] == 1:
                v += 1
            else:
                if v==K:
                    result += 1
                v = 0
        if h==K:
            result += 1
        if v==K:
            result += 1
        v, h = 0, 0
    print(f'#{test_case} {result}')