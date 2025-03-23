from collections import deque

def solution(info, edges):
    answer = 0
    li = len(info)
    tree = [[] for _ in range(li)]
    for e in edges:
        tree[e[0]].append(e[1])
    q = deque([[1,0,tree[0]]])
    while q:
        obj = q.popleft()
        answer = max(answer,obj[0])
        for node in obj[2]:
            next = [x for x in obj[2] if x!=node]
            if info[node]==0 or (info[node]==1 and obj[0]>obj[1]+1):
                if info[node]:
                    q.append([obj[0],obj[1]+1,next+tree[node]])
                else:
                    q.append([obj[0]+1,obj[1],next+tree[node]])
    return answer