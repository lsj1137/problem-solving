def mix(n):
  result = set([])
  ln = list(str(n))
  for i in range(len(ln)):
    for j in range(i+1, len(ln)):
      temp = ln[i]
      ln[i] = ln[j]
      ln[j] = temp
      newN = ''.join(ln)
      result.add(int(newN))
      temp = ln[i]
      ln[i] = ln[j]
      ln[j] = temp
  return result

T = int(input())
for test_case in range(1, T + 1):
  N, c = map(int,input().split())
  que = [N]
  newQue = set([])
  while c>0:
    now = que.pop()
    newQue = newQue.union(mix(now))
    if len(que)==0:
      que = list(newQue)
      newQue = set([])
      c -= 1
  result = max(que)
  print(f'#{test_case} {result}')
