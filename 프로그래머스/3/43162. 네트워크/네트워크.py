def solution(n, computers):
    answer = 0
    node = [[]for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            if computers[i][j]:
                node[i].append(j)
    chk = [False] * (n+1)
    for i in range(n):
        if not chk[i]:
            answer += 1
            dfs(node,i,chk)
    return answer

def dfs(net, i, chk):
    for n in net[i]:
        if not chk[n]:
            chk[n] = True
            dfs(net,n,chk)
    return