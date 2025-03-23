def solution(str1, str2):
    answer = 0
    str1 = list(str1.upper())
    str2 = list(str2.upper())
    A,B = {}, {}
    for i in range(len(str1)-1):
        a = str1[i]+str1[i+1]
        if a.isalpha():
            if a in A:
                A[a] += 1
            else:
                A[a] = 1
    for i in range(len(str2)-1):
        b = str2[i]+str2[i+1]
        if b.isalpha():
            if b in B:
                B[b] += 1
            else:
                B[b] = 1
    inter = 0
    for k in A:
        if k in B:
            inter += min(A[k],B[k])
            B[k] = max(A[k],B[k])
        else:
            B[k] = A[k]
    union = sum([v for v in B.values()])
    print(A)
    print(B)
    print(inter,union)
    if union!=0:
        answer = 65536*inter//union
    else:
        answer = 65536
    return answer