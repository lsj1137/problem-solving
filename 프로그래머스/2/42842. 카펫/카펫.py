def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3,total//2+1):
        if total%i==0 and (i-2)*(total//i-2)==yellow:
            answer.append(total//i)
            answer.append(i)
            break
    return answer