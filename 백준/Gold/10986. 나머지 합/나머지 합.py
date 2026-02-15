# 아이디어
# 1. 주어진 숫자들을 전부 나머지 계산해서 초기 배열 만듦 [ex. 1 2 3 1 2 -> 1(=1%3) 2(=2%3) 0(=3%3) 1(=1%3) 2(=2%3)]
# 2. 누적합 진행하면서 나머지 계산도 같이 함 [ex. 1 2 0 1 2 -> 1 0(=(1+2)%3) 0(=(0+0)%3) 1(=(0+1)%3) 0(=(1+2)%3)]
# 3. 숫자 별로 나머지 나온 갯수 파악해서 1부터 (그 수-1)까지의 합 구해서 결과에 더함
# [ex. 0:3개, 1:2개, 2:0개 -> 1~3까지 합 + 1~1까지의 합 = 6+1 = 7]
# 여기서 0은 본인도 포함해서 1~3까지 더하는데 이유는 본인 혼자만으로도 나누어 떨어지기 때문.
# 0이 아니면 혼자서는 나누어 떨어지지 않는다는 뜻이므로 본인 포함하면 안됨.

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