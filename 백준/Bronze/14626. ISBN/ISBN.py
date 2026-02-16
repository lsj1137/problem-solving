ISBN = list(input())
check = int(ISBN[-1])
ISBN = ISBN[:len(ISBN)-1]

ISBN_sum = 0
multiply = 1
for i,n in enumerate(ISBN):
    if n=='*':
        multiply = 1 if i%2==0 else 3
        continue
    if i%2==0:
        ISBN_sum += int(n)
    else:
        ISBN_sum += int(n)*3

answer = 0
for i in range(1,10):
    if (ISBN_sum + check+ multiply*i)%10 == 0:
        answer = i
        break
print(answer)