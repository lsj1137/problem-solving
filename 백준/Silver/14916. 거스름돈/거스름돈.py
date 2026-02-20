N = int(input())
result = -1
for i in range(N//5, -1, -1):
    if (N-5*i)%2==0:
        break
if i==0 and (N-5*i)%2!=0:
    result = -1
else:
    result = i+(N-5*i)//2
print(result)