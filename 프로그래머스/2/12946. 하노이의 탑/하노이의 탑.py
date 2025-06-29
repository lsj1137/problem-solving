def hanoi(s, m, e, n):
    result = []
    if n==1:
        result.append([s, e])
    else:
        result = hanoi(s, e, m, n-1) + [[s,e]] + hanoi(m, s, e, n-1)
    return result 
    
def solution(n):
    answer = hanoi(1, 2, 3, n)
    return answer