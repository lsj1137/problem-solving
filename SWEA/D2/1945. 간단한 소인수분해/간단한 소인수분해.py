def div(n, p):
    result = 0
    while n%p==0:
        result += 1
        n //= p
    return (n, result)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    N, e = div(N, 11)
    N, d = div(N, 7)
    N, c = div(N, 5)
    N, b = div(N, 3)
    N, a = div(N, 2)
    answer = f'{a} {b} {c} {d} {e}'
    print(f'#{test_case} {answer}')