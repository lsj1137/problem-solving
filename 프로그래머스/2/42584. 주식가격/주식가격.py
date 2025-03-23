def solution(prices):
    answer = [0]*len(prices)
    st = []
    for i in range(len(prices)):
        if st:
            while st and prices[i]<st[-1][0]:
                obj = st.pop()
                answer[obj[1]] = i - obj[1]
        st.append((prices[i],i))
    while st:
        obj = st.pop()
        answer[obj[1]] = i - obj[1]
    return answer