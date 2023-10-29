p = int(input())
dic = dict()
for _ in range(p):
    fruit, num = input().split()
    if fruit not in dic:
        dic[fruit] = int(num)
    else:
        dic[fruit] += int(num)
for d in dic.items():
    if d[1] == 5:
        print('YES')
        break
else:
    print('NO')