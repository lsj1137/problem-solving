def solution(arr):
    answer = -1
    MAX_SIZE = 99999999
    N = len(arr)//2 + 1
    maxArr = [[-MAX_SIZE]*N for _ in range(N)]
    minArr = [[MAX_SIZE]*N for _ in range(N)]
    
    for step in range(N):
        for i in range(N-step):
            
            j = i+step
            
            if step==0:
                maxArr[i][j] = int(arr[i*2])
                minArr[i][j] = int(arr[i*2])
            else:
                for k in range(i,j):
                    if arr[k*2+1]=='+':
                        maxArr[i][j] = max(maxArr[i][j], maxArr[i][k]+maxArr[k+1][j])
                        minArr[i][j] = min(minArr[i][j], minArr[i][k]+minArr[k+1][j])
                    else:
                        maxArr[i][j] = max(maxArr[i][j], maxArr[i][k]-minArr[k+1][j])
                        minArr[i][j] = min(minArr[i][j], minArr[i][k]-maxArr[k+1][j])
            # print('i, step:', i, step)
            # print(maxArr[i][j],minArr[i][j])
            # print('======')
    answer = maxArr[0][N-1]
    return answer