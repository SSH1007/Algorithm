N = int(input())
dic = {}
for _ in range(N):
    A, B = input().split()
    if not A in dic:
        dic[A] = 0
    if not B in dic:
        dic[B] = 0
    if A == 'ChongChong' or B == 'ChongChong':
        dic[A] = 1
        dic[B] = 1
    if dic[A] == 1 or dic[B] == 1:
        dic[A] = 1
        dic[B] = 1
print(sum(dic.values()))