import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    tmp = []
    for _ in range(4):
        a, b = map(int, input().rstrip().split())
        tmp.append((a, b))
    tmp.sort(key= lambda x:(x[0],x[1]))
    lst = []
    for i in range(4):
        for j in range(i+1, 4):
            x = abs(tmp[i][1]-tmp[j][1])
            y = abs(tmp[i][0]-tmp[j][0])
            lst.append((x**2+y**2)**0.5)
    lst.sort()
    if lst[0] == lst[1] and lst[1] == lst[2] and lst[2] == lst[3] and lst[4] == lst[5]:
        print(1)
    else:
        print(0)