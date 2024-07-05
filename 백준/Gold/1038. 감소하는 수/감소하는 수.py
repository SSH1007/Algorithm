from itertools import combinations
N = int(input())
# 9876543210
lst = []
for i in range(1, 11):
    for combo in combinations(range(10), i):
        lst.append(int(''.join(list(map(str, combo))[::-1])))
lst.sort()
if len(lst) <= N:
    print(-1)
else:
    print(lst[N])