N = int(input())
w_list = [input() for _ in range(N)]
c_dict = {}
num_mapper = {}
result = 0

max_w = max(w_list, key=len)
M = len(max_w)

new_w_list = []
for w in w_list:
    new_w_list.append(w.zfill(M))

num = 9
for i in range(M):
    for w in new_w_list:
        n = w[i]
        if n != '0':
            if n in c_dict:
                c_dict[n] += 10**(M-i)
            else:
                c_dict[n] = 10**(M-i)
                
sorted_c = sorted(list(c_dict.items()), key=lambda x:x[1], reverse=True)
for sortc in sorted_c:
    num_mapper[sortc[0]] = str(num)
    num -= 1

for w in w_list:
    new_w = ''
    for c in w:
        new_w += num_mapper[c]
    result += int(new_w)
print(result)
