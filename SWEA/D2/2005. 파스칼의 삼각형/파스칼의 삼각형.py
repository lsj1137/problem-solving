T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tri = [[1]]
    for i in range(2, N+1):
        line = []
        for j in range(i):
            if j-1<0:
                l = 0
            else:
                l = tri[-1][j-1]
            if j>len(tri[-1])-1:
                r = 0
            else:
                r = tri[-1][j]
            line.append(l+r)
        tri.append(line)
    print(f'#{test_case}')
    for line in tri:
        print(*line)