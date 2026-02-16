import math

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_order = 0
pen_group_order = 0
pen_one_order = 0

for s in size:
    shirt_order += math.ceil(s/T)

pen_group_order = N//P
pen_one_order = N%P

print(shirt_order)
print(pen_group_order, pen_one_order)