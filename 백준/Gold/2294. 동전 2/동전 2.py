import sys; ip = sys.stdin.readline

N,K = map(int,ip().split())
coin = sorted([int(ip()) for _ in range(N)])

price = [float('inf')]*(K+1)
for i in range(N):
  if coin[i]<=K:
    price[coin[i]] = 1

for i in range(len(price)):
  for c in coin:
    if c>i:
      break
    price[i] = min(price[i], price[i-c]+1)

print(price[-1] if price[-1]!=float('inf') else -1)
