import math
# N = len(Alst)
N = int(input())
Alst = list(map(int, input().split()))
B, C = map(int, input().split())

dap = 0
for a in Alst:
    dap+=1
    if a-B > 0:
        dap+=math.ceil((a-B)/C)
print(dap)