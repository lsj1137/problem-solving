import sys
input = sys.stdin.readline

K, L = map(int, input().strip().split())
seq = {}
for i in range(L):
    id = input().strip()
    seq[id] = i

final_seq = sorted(list(seq.keys()), key=lambda x:seq[x])
success = final_seq[:K]
for student in success:
    print(student)