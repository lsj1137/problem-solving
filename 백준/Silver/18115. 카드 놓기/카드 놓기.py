from collections import deque

N = int(input())
cmd_arr = list(input().split())[::-1]
result = deque([])
for i in range(N):
    cmd = cmd_arr[i]
    if cmd=='1':
        result.appendleft(i+1)
    elif cmd=='2':
        tmp = result.popleft()
        result.appendleft(i+1)
        result.appendleft(tmp)
    else:
        result.append(i+1)
print(*result)