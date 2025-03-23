N = int(input())
if N%2==0:
    N//=2
    if N%2==0:
        print("2")
    else:
        print("1")
else:
    print("0")