def solution(n):
    answer = []
    while n>0:
        if n%3==0 :
            answer.append(4)
            n -= 3
        else:
            answer.append(n%3)
        n //= 3 
    answer = answer[::-1]
    answer = map(str,answer)
    answer = ''.join(answer)
    return answer