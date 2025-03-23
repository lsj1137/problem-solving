def solution(rows, columns, queries):
    answer = []
    table = [[] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            table[i].append(columns*i+j+1)
    for q in queries:
        x1, y1 = q[0]-1, q[1]-1
        x2, y2 = q[2]-1, q[3]-1
        n = rows*columns+1
        tmp1 = table[x1][y1]
        for i in range(y1,y2):
            n = min(tmp1,n)
            tmp2 = table[x1][i+1]
            table[x1][i+1] = tmp1
            tmp1 = tmp2
        for i in range(x1,x2):
            n = min(tmp1,n)
            tmp2 = table[i+1][y2]
            table[i+1][y2] = tmp1
            tmp1 = tmp2
        for i in range(y2,y1,-1):
            n = min(tmp1,n)
            tmp2 = table[x2][i-1]
            table[x2][i-1] = tmp1
            tmp1 = tmp2
        for i in range(x2,x1,-1):
            n = min(tmp1,n)
            tmp2 = table[i-1][y1]
            table[i-1][y1] = tmp1
            tmp1 = tmp2
        answer.append(n)
    return answer