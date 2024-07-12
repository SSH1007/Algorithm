# 9876543210
def DFS(l, num):
    if l == 1:
        lst.append(num)
        return
    for i in range(int(str(num)[-1])-1, -1, -1):
        DFS(l-1, num*10+i)


N = int(input())
if N > 1023:
    print(-1)
else:
    lst = []
    # 자리수 (1자리부터 10자리)
    for i in range(1, 11):
        # 맨 앞에 위치할 수(9~0)
        for j in range(9, -1, -1):
            DFS(i, j)
    lst.sort()
    print(lst[N-1])