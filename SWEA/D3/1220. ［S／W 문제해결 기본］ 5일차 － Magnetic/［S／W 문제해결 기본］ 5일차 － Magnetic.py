def move(table):
    moved = False
    for i in range(100):
        for j in range(100):
            if table[i][j]=='1':
                if i+1<100 and table[i+1][j]!='2':
                    table[i][j] = '0'
                    table[i+1][j] = '1'
                    moved = True
                elif i+1>99:
                    table[i][j] = '0'
                    moved = True
            if table[i][j]=='2':
                if i-1>-1 and table[i-1][j]!='1':
                    table[i][j] = '0'
                    table[i-1][j] = '2'
                    moved = True
                elif i-1<0:
                    table[i][j] = '0'
                    moved = True
    return moved

def checkStale(table):
    result = 0
    for j in range(100):
        for i in range(100):
            if table[i][j]=='1' and table[i+1][j]=='2':
                result += 1
    return result

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    table = [list(input().split()) for _ in range(N)]
    while True:
        if not move(table):
            break
    answer = checkStale(table)
    print(f'#{test_case} {answer}')