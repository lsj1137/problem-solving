def solution(board, moves):
    answer = 0
    st = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1]!=0:
                st.append(board[i][m-1])
                board[i][m-1] = 0
                break
        while len(st)>1 and st[-1]==st[-2]:
            st.pop()
            st.pop()
            answer += 2
    return answer