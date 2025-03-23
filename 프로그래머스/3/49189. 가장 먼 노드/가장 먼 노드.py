def solution(n, edge):
    answer = 0
    nodes = [[] for _ in range(n+1)]
    chk = [False]*(n+1)
    for e in edge:
        nodes[e[0]].append(e[1])
        nodes[e[1]].append(e[0])
    node = nodes[1]
    chk[1] = True
    newnode = []
    ans = 0
    while node:
        n = node.pop()
        if not chk[n]:
            ans += 1
            chk[n] = True
            newnode += nodes[n]
            answer = ans
        if not node:
            ans = 0
            node = newnode
            newnode = []
    return answer