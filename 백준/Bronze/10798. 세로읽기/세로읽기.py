import sys
input = sys.stdin.readline
ys = [[0 for _ in range(15)] for _ in range(5)]
maxlen = 0
for i in range(5):
    lst = input().rstrip()
    if maxlen < len(lst):
        maxlen = len(lst)
    for j in range(len(lst)):
        ys[i][j] = lst[j]
for i in range(maxlen):
    for j in range(5):
        if ys[j][i] == 0:
            continue
        print(ys[j][i], end='')