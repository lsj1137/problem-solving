m = int(input())
d = int(input())
if m<2:
  print("Before")
elif m>2:
  print("After")
else:
  if d<18:
    print("Before")
  elif d>18:
    print("After")
  else:
    print("Special")