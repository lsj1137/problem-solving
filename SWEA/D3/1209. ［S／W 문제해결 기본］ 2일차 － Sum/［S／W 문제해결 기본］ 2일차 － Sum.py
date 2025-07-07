T = 10
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sums = []
    for i in range(100):
        sums.append(sum(arr[i][j] for j in range(100)))
        sums.append(sum(arr[j][i] for j in range(100)))
    sums.append(sum(arr[i][i] for i in range(100)))
    sums.append(sum(arr[i][99-i] for i in range(100)))

    answer = max(sums)

    print(f'#{test_case} {answer}')