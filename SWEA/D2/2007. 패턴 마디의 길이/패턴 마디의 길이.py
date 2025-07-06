T = int(input())
for test_case in range(1, T + 1):
    S = input()
    result = 0
    for l in range(1, 10):
        p = S[:l]
        for r in range(l, len(S)-l, l):
            if p == S[r:r+l]:
                result = l
            else:
                result = 0
                break
        if result!=0:
            break    
    print(f'#{test_case} {result}')