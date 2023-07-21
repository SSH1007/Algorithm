N = int(input())
student = [[i, []] for i in range(N+1)]
info = []
for _ in range(N):
    data = list(map(int, input().split()))
    info.append(data)

for i in range(5):
    dic = dict()
    for j in range(N):
        if info[j][i] not in dic:
            dic[info[j][i]] = [j+1]
        else:
            dic[info[j][i]].append(j+1)
    # print(dic)
    for value in dic.values():
        if len(value) > 1:
            for v in value:
                for vv in value:
                    if v != vv:
                        student[v][1].append(vv)

for s in student:
    s[1] = list(set(s[1]))
student = student[1:]
student.sort(key=lambda x: (-len(x[1]), x[0]))
print(student[0][0])