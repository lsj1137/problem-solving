# 3진법 변형
# -> 0이 나오면 4로 바꾸고 앞자리 1 내려야 함
# -> 애초에 3으로 나누어떨어지면 4를 넣고 -3 해버림
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