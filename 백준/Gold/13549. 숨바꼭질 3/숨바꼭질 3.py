from collections import deque

N, K = map(int, input().split())
MAX_POS = 100001
dist = [-1] * MAX_POS

def bfs():
    que = deque([N])
    dist[N] = 0
    
    while que:
        cur = que.popleft()
        
        if cur == K:
            return dist[cur]
            
        # 순간이동 (0초) - 우선순위가 높으므로 먼저 처리 appendleft
        if 0 < cur * 2 < MAX_POS and dist[cur * 2] == -1:
            dist[cur * 2] = dist[cur]
            que.appendleft(cur * 2)
            
        # 걷기 (1초) - append
        for move in [cur - 1, cur + 1]:
            if 0 <= move < MAX_POS and dist[move] == -1:
                dist[move] = dist[cur] + 1
                que.append(move)

print(bfs())