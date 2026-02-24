import sys
import re
input = sys.stdin.readline
pattern = re.compile('(100+1+|01)+')

for _ in range(int(input())):
    data = input().strip()
    if pattern.fullmatch(data):
        print("YES")
    else:
        print("NO")
