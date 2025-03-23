def solution(numbers, target):
    answer = cal(numbers,0,0,target)
    return answer

def cal(nl,i,r,g):
    if i==len(nl):
        if r==g:
            return 1
        else:
            return 0
    else:
        return cal(nl,i+1,r + nl[i],g)+cal(nl,i+1,r - nl[i],g)