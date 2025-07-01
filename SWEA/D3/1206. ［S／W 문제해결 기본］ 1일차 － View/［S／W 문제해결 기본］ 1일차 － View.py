T = 10
for test_case in range(1, T + 1):
  N = int(input())
  result = 0
  buildings = list(map(int,input().split()))
  for i in range(2,N-2):
    a,b,c,d = buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]
    maxi = max(a,b,c,d)
    if buildings[i] > maxi:
      result += buildings[i]-maxi
  print(f'#{test_case} {result}')
