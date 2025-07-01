def canLocate(checked, x, y):
    nx = x-1
    ny1 = y-1
    ny2 = y+1
    while nx>-1:
        if checked[nx][y]:
            return False
        elif ny1>-1 and checked[nx][ny1]:
            return False
        elif ny2<len(checked) and checked[nx][ny2]:
            return False
        nx -= 1
        ny1 -= 1
        ny2 += 1
    return True

def dfs(checked, x):
    result = 0
    if x==len(checked)-1:
        return 1
    for ny in range(len(checked)):
        if canLocate(checked, x+1, ny):
            checked[x+1][ny] = True
            result += dfs(checked, x+1)
            checked[x+1][ny] = False
    return result

T = int(input())
for test_case in range(1, T + 1):
  n = int(input())
  answer = 0
  checked = [[False for _ in range(n)] for _ in range(n)]
  answer += dfs(checked,-1)
  print(f'#{test_case} {answer}')