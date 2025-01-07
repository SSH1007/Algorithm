N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
s = sorted(lst, reverse=True)
e = sorted(lst, key=lambda x: x[1])
tmp = s[0][0]-e[0][1]
if tmp < 0:
    print(0)
else:
    print(tmp)