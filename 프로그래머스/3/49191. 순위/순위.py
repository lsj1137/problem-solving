def solution(n, results):
    answer = 0
    graph = [[0]*(n+1) for _ in range(n+1)]
    for win, lose in results:
        graph[win][lose] = 1
        graph[lose][win] = -1
        
    for i in range(1,n+1):
        for j in range(1, n+1):
            if graph[i][j]==1:
                for k in range(1, n+1):
                    if k!=i and graph[j][k]==1:
                        graph[i][k] = 1
            if graph[i][j]==-1:
                for k in range(1, n+1):
                    if k!=i and graph[j][k]==-1:
                        graph[i][k] = -1
    for i in range(1,n+1):
        for j in range(1, n+1):
            if graph[i][j]==1:
                for k in range(1, n+1):
                    if k!=i and graph[j][k]==1:
                        graph[i][k] = 1
            if graph[i][j]==-1:
                for k in range(1, n+1):
                    if k!=i and graph[j][k]==-1:
                        graph[i][k] = -1
    for g in graph:
        temp = 0
        for n in g[1:]:
            if n==0:
                temp+=1
        if temp==1:
            answer += 1
    
    return answer