N = int(input())
tanghooroo = list(map(int, input().split()))
type_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
type_dict[tanghooroo[0]] += 1
type_set = set([tanghooroo[0]])
type_cnt = len(type_set)

result = 1
e = 0
for s in range(N-1):
    while type_cnt<=2 and e<N-1:
        e += 1
        new_fruit = tanghooroo[e]
        type_dict[new_fruit] += 1
        if new_fruit not in type_set:
            type_set.add(new_fruit)
            type_cnt += 1
    result = max(result, e-s+1 if type_cnt<=2 else e-s)
    old_fruit = tanghooroo[s]
    type_dict[old_fruit] -= 1
    if type_dict[old_fruit] == 0:
        type_set.remove(old_fruit)
        type_cnt -= 1
print(result)