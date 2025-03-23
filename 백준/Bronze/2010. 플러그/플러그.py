import sys; ip = sys.stdin.readline
m = int(ip())
r = -m+1
for _ in range(m):
    r += int(ip())
print(r)