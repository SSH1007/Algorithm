N = int(input())
arr = []
for i in range(N+1):
    tmp = N
    tmparr = [tmp,i]
    midarr = [i]
    while 1:
        sec = tmparr.pop()
        fir = tmparr.pop()
        if fir-sec<0:
            break
        tmparr.append(sec)
        tmparr.append(fir-sec)
        midarr.append(fir-sec)
    if len(arr) < len(midarr):
        arr = midarr
arr = [N] + arr
print(len(arr))
print(*arr)