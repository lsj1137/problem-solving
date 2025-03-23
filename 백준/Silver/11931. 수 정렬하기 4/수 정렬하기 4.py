import sys
nl = []
for _ in range(int(sys.stdin.readline())):
  nl.append(int(sys.stdin.readline()))
nl.sort(reverse= True)
for n in nl:
  print(n)