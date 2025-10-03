def solution(n, costs):
    answer = 0
    checked = [False]*n
    route = [[] for _ in range(n)]
    for cost in costs:
        a,b,c = cost
        route[a].append([b,c])
        route[b].append([a,c])
    # print(route)
    que = route[0]
    checked[0] = True
    que.sort(key= lambda x: -x[1])
    # print(que)
    while len(que)>0:
        nextNode, cost = que.pop()
        if not checked[nextNode]:
            answer += cost
            checked[nextNode] = True
        for r in route[nextNode]:
            if not checked[r[0]]:
                que.append(r)
        que.sort(key= lambda x: -x[1])
        # print(que)
    return answer