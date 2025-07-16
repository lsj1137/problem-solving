T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    answer = 0
    for i in range(1, N+1):
        answer += i if i%2!=0 else -i
    print(f'#{test_case} {answer}')