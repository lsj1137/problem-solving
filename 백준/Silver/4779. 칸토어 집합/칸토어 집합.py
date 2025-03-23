import sys

def canto(n) :
    if n==0:
        return "-"
    return canto(n-1) + " "*(3**(n-1)) + canto(n-1)

while True:
    try:
        print(canto(int(input())))
    except:
        break