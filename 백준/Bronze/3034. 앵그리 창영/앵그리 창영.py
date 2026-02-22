N, W, H = map(int, input().split())
max_len = (W**2 + H**2)**0.5
for _ in range(N):
    match = int(input())
    if match<=max_len:
        print("DA")
    else:
        print("NE")
