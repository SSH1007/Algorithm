puzzle = [list(input()) for _ in range(4)]
dap = 0
for i in range(4):
    for j in range(4):
        if puzzle[i][j] != '.':
            o = ord(puzzle[i][j])
            r = (o-65)//4
            c = (o-65)-(4*r)
            dap += abs(i-r)+abs(j-c)
print(dap)