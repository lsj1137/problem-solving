import sys
N = int(sys.stdin.readline())
wl = [0]+list(map(int,sys.stdin.readline().split()))
wl.sort()
for i in range(N+1):
  if i==N:
    print(sum(wl)+1)
    break
  elif sum(wl[:i+1])+1<wl[i+1]:
    print(sum(wl[:i+1])+1)
    break