N = input()
n = list(map(int,input().split()))
w = n.copy()
n.sort()
for i in range(len(w)):
  o = n.index(w[i])
  print(o,end=" ")
  n[o] = str(n[o])