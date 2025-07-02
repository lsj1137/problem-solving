T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = [list(input()) for _ in range(N)]
    answer = 0
    center = N//2
    for i in range(N):
        if i<=center:
            for j in range(center-i, center-i+2*i+1):
                answer += int(farm[i][j])
        else:
            for j in range(i-center, i-center+2*(N-i)-1):
                answer += int(farm[i][j])

    print(f'#{test_case} {answer}')