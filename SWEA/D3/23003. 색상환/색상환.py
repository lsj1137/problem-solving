pallete = {"red":1, "orange":2, "yellow":3, "green":4, "blue":5, "purple":6}
for t in range(int(input())):
  c1, c2 = input().split()
  if pallete[c1] == pallete[c2]:
    print('E')
  elif abs(pallete[c1] - pallete[c2]) == 1 or abs(pallete[c1] - pallete[c2]) == 5:
    print('A')
  elif abs(pallete[c1] - pallete[c2]) == 3:
    print('C')
  else :
    print('X')
