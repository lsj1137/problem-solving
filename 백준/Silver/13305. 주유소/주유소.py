import sys
N = int(sys.stdin.readline())
dist = list(map(int,sys.stdin.readline().split()))
oil = list(map(int,sys.stdin.readline().split()))

i = 0
cheap = oil[0]
total = cheap*dist[0]
while i<N-2:
  i+=1
  if oil[i]<cheap:
    cheap = oil[i]
  total += dist[i]*cheap
print(total)