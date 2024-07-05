N = int(input())
# 9876543210
dap = []


def DFS(num):
    dap.append(num)
    std = str(num)[0]
    for i in range(int(std)+1, 10):
        DFS(int(str(i)+str(num)))


for i in range(10):
    DFS(i)
dap.sort()
try:
    print(dap[N])
except:
    print(-1)