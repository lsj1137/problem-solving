n = int(input())

money = [0 for _ in range(n+1)]
for i in range(n):
    t,p = map(int,input().split())
    for j in range(i+t,n+1):
        money[j] = max(money[j], money[i]+p)
print(money[n])
