tmps = []
while 1:
    n = float(input())
    if n==999:
        break
    tmps.append(n)
    if len(tmps)==2:
        print(f'{tmps[1]-tmps[0]:.2f}')
        tmps=tmps[::-1]
        tmps.pop()