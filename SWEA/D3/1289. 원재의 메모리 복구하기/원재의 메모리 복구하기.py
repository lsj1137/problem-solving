T = int(input())
for test_case in range(1, T + 1):
    S = input()
    curBit = '0'
    answer = 0
    for c in S:
        if c==curBit:
            continue
        else:
            if curBit=='0':
                curBit = '1'
            else:
                curBit = '0'
            answer += 1
    print(f'#{test_case} {answer}')