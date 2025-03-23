def solution(places):
    answer = []
    for k in range(5):
        chk = [[False]*5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    chk[i][j] = True
                    if not dfs(places[k],i,j,chk,0):
                        answer.append(0)
                        break
            if len(answer) == k+1:
                break
        if len(answer) == k:
            answer.append(1)
    return answer

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(r,x,y,chk,d):
    if d==2:
        return True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<5 and -1<ny<5 and not chk[nx][ny]:
            chk[nx][ny] = True
            if r[nx][ny] == 'X':
                continue
            elif r[nx][ny] == 'P':
                return False
            if not dfs(r,nx,ny,chk,d+1):
                return False
    return True