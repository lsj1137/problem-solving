n = int(input())
for i in range(n):
  if i%2==0:
    print("* "*n,end="")
  else:
    print(" *"*n,end="")
  print()