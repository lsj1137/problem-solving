T = int(input())
for test_case in range(1, T + 1):
    N = input()
    nSet = set(list(N))
    N = int(N)
    answer = N
    while len(nSet)<10:
        answer += N
        nSet = nSet.union(set(list(str(answer))))
    print(f'#{test_case} {answer}')