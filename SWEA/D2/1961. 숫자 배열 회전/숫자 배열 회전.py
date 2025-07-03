def spin(N, arr):
    result = []
    for i in range(N):
        line = []
        for j in range(N-1,-1,-1):
            line.append(arr[j][i])
        result.append(line)
    return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    spin90 = spin(N, arr)
    spin180 = spin(N, spin90)
    spin270 = spin(N, spin180)
    print(f'#{test_case}')
    for i in range(N):
        print(''.join(spin90[i]), ''.join(spin180[i]),''.join(spin270[i]))