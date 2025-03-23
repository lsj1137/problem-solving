N = int(input())
start = 64
stack = 0
c = 0
if N == start:
  c = 1
else:
  while stack<N:
    start //= 2
    if stack + start < N+1:
      stack += start
      c+= 1
    else:
      continue
print(c)