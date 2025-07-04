def mulSum(l1, l2, s):
    suml = 0
    for i in range(s, s+len(l1)):
        suml += l1[i-s] * l2[i]
    return suml

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    result = 0
    if len(l1)>len(l2):
        l1, l2 = l2, l1
    for i in range(len(l2)-len(l1)+1):
        result = max(result, mulSum(l1, l2, i))
    print(f'#{test_case} {result}')