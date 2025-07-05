def checkPel(arr):
    s,e = 0, len(arr)-1
    while s<e:
        if arr[s]!=arr[e]:
            return False
        s+=1
        e-=1
    return True

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    result = 0
    for i in range(8):
        for j in range(8-N+1):
            s1 = []
            s2 = []
            for k in range(N):
                s1.append(board[i][j+k])
                s2.append(board[j+k][i])
            if checkPel(s1):
                result += 1
            if checkPel(s2):
                result += 1
    print(f'#{test_case} {result}')