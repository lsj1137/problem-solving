from itertools import combinations

s_dict = {}
result = 0
for _ in range(int(input())):
    s = input()
    c_dict = {}
    c_cnt = 0
    new_s = ''
    for c in s:
        if c not in c_dict:
            c_dict[c] = str(c_cnt)
            c_cnt += 1
        new_s += c_dict[c]

    if new_s in s_dict:
        s_dict[new_s] += 1
    else:
        s_dict[new_s] = 1

for v in s_dict.values():
    result += len(list(combinations(range(v),2)))

print(result)