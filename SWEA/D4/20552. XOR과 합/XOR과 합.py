T = int(input())
for _ in range(T):
    X, S = map(int, input().split())
    
    if X > S or (S - X) % 2 != 0:
        print(-1)
        continue

    if X == 0 and S == 0:
        print(0)
        continue

    if X == S:
        print(1)
        print(X)
        continue

    a = (S - X) // 2

    # Check if a & X == 0
    if a & X == 0:
        print(2)
        print(a, a + X)
    else:
        print(3)
        print(a, a, X)