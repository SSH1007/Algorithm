# del과 insert
N = int(input())
vid = list(map(int, input().split()))
dap = 0


def getEnergy(energy):
    global dap
    if len(vid) == 2:
        if energy > dap:
            dap = energy
        return
    for x in range(1, len(vid)-1):
        generate = vid[x-1]*vid[x+1]
        middle = vid[x]
        del vid[x]
        getEnergy(energy+generate)
        vid.insert(x, middle)


getEnergy(0)
print(dap)