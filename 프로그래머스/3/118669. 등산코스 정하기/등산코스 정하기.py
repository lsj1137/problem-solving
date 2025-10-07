import heapq

def solution(n, paths, gates, summits):
    MAX_NUM = float('inf')
    answer = [MAX_NUM, MAX_NUM]
    
    routes = [[]*(n+1) for _ in range(n+1)]
    for p in paths:
        a,b,dist = p
        routes[a].append([dist,b])
        routes[b].append([dist,a])
        
    dpArr = [MAX_NUM]*(n+1) # 각 지점까지의 intensity
    gatesSet, summitsSet = set(gates), set(summits)
    que = []
    for g in gates:
        heapq.heappush(que, [0, g])
    while len(que)>0:
        curInt, curNode = heapq.heappop(que)
        if curNode in summitsSet:
            continue
        if curInt > dpArr[curNode]:
            continue
        for nextDist, nextNode in routes[curNode]:
            if nextNode in gatesSet:
                continue
            newInt = max(curInt, nextDist)
            if newInt >= dpArr[nextNode]:
                continue
            dpArr[nextNode] = min(dpArr[nextNode], newInt)
            heapq.heappush(que, [dpArr[nextNode], nextNode])
    answers = []
    for i in range(n+1):
        if i in summitsSet:
            answers.append([i,dpArr[i]])
    answers.sort(key = lambda x:(x[1],x[0]))
    answer = answers[0]
    return answer