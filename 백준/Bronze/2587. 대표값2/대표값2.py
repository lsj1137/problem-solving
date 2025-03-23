nl = []
for _ in range(5):
    nl.append(int(input()))
nl.sort()
print(sum(nl)//5)
print(nl[2])