T = int(input())
for test_case in range(1, T + 1):
    S = input()
    answer = 1
    for i in range(len(S)//2):
        if S[i] != S[len(S)-1-i]:
            answer = 0
    print(f'#{test_case} {answer}')