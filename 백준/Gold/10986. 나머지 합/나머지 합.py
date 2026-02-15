def sum_until(n):
    return n*(n+1)//2

N, M = map(int, input().split())
num_arr = list(map(lambda x:int(x)%M, input().split()))
result = 0
remain_cnt = {}
for i in range(M):
    remain_cnt[i]=0

for i in range(N):
    if i==0:
        remain_cnt[num_arr[i]] += 1
        continue
    num_arr[i] = (num_arr[i] + num_arr[i-1]) % M
    remain_cnt[num_arr[i]] += 1

result += sum_until(remain_cnt[0])
for i in range(1, M):
    result += sum_until(remain_cnt[i]-1)

print(result)