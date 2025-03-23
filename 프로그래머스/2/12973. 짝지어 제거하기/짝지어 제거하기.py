def solution(s):
    answer = -1
    st = []
    for c in s:
        st.append(c)
        while len(st)>1:
            if st[-1]==st[-2]:
                st.pop()
                st.pop()
            else:
                break
    if st:
        answer = 0
    else:
        answer = 1
    return answer