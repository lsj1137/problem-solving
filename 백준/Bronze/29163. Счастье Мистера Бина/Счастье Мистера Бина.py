N = int(input())
nl = list(map(int,input().split()))
odd, even = 0, 0

for n in nl:
    if n%2==0:
        even += 1
    else:
        odd += 1
if even>odd:
    print("Happy")
else:
    print("Sad")