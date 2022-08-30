i = []
m = []
for _ in range(4):
    i.append(int(input()))
for _ in range(2):
    m.append(int(input()))
i.sort(reverse=True)
m.sort(reverse=True)
print(i[0]+i[1]+i[2]+m[0])