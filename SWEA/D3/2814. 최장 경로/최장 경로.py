def dfs(cur, nodes, checked, depth):
    result = depth
    nextNodes = nodes[cur]
    for n in nextNodes:
        if not checked[n]:
            checked[n] = True
            result = max(result, dfs(n, nodes, checked, depth+1))
            checked[n] = False
    return result

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int, input().split())
    nodes = [[] for _ in range(N)]
    checked = [False for _ in range(N)]
    for _ in range(M):
        x,y = map(int, input().split())
        nodes[x-1].append(y-1)
        nodes[y-1].append(x-1)
    answer = 1
    for i in range(N):
        checked[i] = True
        answer = max(answer, dfs(i, nodes, checked, 1))
        checked[i] = False
    print(f'#{test_case} {answer}')