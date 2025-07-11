T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int,input().split())
    customers = sorted(list(map(int,input().split())))
    t = 0
    bbang = 0
    i = 0
    answer = "Possible"
    while t<=customers[-1]:
        while i<len(customers) and customers[i]<=t:
            if bbang>0:
                bbang -= 1
            else:
                answer = "Impossible"
                break
            i += 1
        if answer == "Impossible":
            break
        t += 1
        if t%M==0:
            bbang += K
    print(f'#{test_case} {answer}')