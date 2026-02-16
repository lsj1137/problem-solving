import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nl = list(map(int, input().split()))
answer = float('inf')

s,e = 0,0
part_sum = nl[0]
while s<N and e<N:
    if part_sum<S:
        e+=1
        if e>N-1:
            break
        part_sum += nl[e]
    else:
        answer = min(answer, e-s+1)
        if s==e:
            e+=1
            if e<N:
                part_sum += nl[e]
        part_sum -= nl[s]
        s+=1

if answer == float('inf'):
    answer = 0
print(answer)