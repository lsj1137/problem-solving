def solution(board, skill):
    answer = 0
    R = len(board)
    C = len(board[0])
    new = [[0]*(C+1) for _ in range(R+1)]
    for s in skill:
        if s[0]==1:
            new[s[3]+1][s[2]] += s[5]
            new[s[3]+1][s[4]+1] -= s[5]
            new[s[1]][s[2]] -= s[5]
            new[s[1]][s[4]+1] += s[5]
        else:
            new[s[3]+1][s[2]] -= s[5]
            new[s[3]+1][s[4]+1] += s[5]
            new[s[1]][s[2]] += s[5]
            new[s[1]][s[4]+1] -= s[5]
    for i in range(R):
        for j in range(1,C):
            new[i][j] += new[i][j-1]
    for i in range(C):
        for j in range(1,R):
            new[j][i] += new[j-1][i]
    #print(new)
    for i in range(R):
        for j in range(C):
            if board[i][j] + new[i][j]>0:
                answer += 1
    return answer