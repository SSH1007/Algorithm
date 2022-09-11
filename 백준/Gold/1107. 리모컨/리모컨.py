N = int(input())
dap = abs(N-100)
M = int(input())
if M == 0:
    broken = []
else:
    broken = list(input().split())

for channel in range(1000001):
    for i in str(channel):
        if i in broken:
            break
    else:
        dap = min(dap, len(str(channel))+abs(channel-N))
        
print(dap)