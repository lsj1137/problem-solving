T = 10
for test_case in range(1, T + 1):
    n = int(input())
    nl = list(map(int,input().split()))
    nl.sort()
    while n>0:
        if nl[-1]-nl[0]<=1:
            break
        nl[-1]-=1
        nl[0]+=1
        nl.sort()
        n-=1
    answer = nl[-1]-nl[0]
    print(f'#{test_case} {answer}')