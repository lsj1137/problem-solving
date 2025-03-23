def solution(answers):
    answer = []
    la = len(answers)
    A = [1,2,3,4,5]*(la//5) + [1,2,3,4,5][:la%5]
    B = [2,1,2,3,2,4,2,5]*(la//8) + [2,1,2,3,2,4,2,5][:la%8]
    C = [3,3,1,1,2,2,4,4,5,5]*(la//10) + [3,3,1,1,2,2,4,4,5,5][:la%10]
    print(A)
    print(B)
    print(C)
    a,b,c = 0,0,0
    for i in range(la):
        if answers[i]==A[i]:
            a+=1
        if answers[i]==B[i]:
            b+=1
        if answers[i]==C[i]:
            c+=1
    maxi = max(a,b,c)
    if maxi == a:
        answer.append(1)
    if maxi == b:
        answer.append(2)
    if maxi == c:
        answer.append(3)
    return answer