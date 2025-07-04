T = 10
for test_case in range(1, T + 1):
    N = int(input())
    dx = [-1, 0, 0]
    dy = [0, -1, 1]
    di = 0
    ladder = [list(input().split()) for _ in range(100)]
    s = 0
    for i in range(100):
        if ladder[-1][i]=='2':
            s = i
            break
    cx, cy = 99, s
    while cx>0:
        if di==0 and cy-1>-1 and ladder[cx][cy-1]=='1':
            di = 1
        elif di==0 and cy+1<100 and ladder[cx][cy+1]=='1':
            di = 2
        elif di!=0 and (cy+dy[di]<0 or cy+dy[di]>99):
            di = 0
        elif di!=0 and cy+dy[di]>-1 and cy+dy[di]<100 and ladder[cx][cy+dy[di]]=='0':
            di = 0
        cx, cy = cx+dx[di], cy+dy[di]
    result = cy
    print(f'#{test_case} {result}')