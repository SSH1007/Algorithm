pan = [[0]*8 for _ in range(8)]
dr = {'R':0, 'L':0, 'B':1, 'T':-1, 'RT':-1, 'LT':-1, 'RB':1, 'LB':1}
dc = {'R':1, 'L':-1, 'B':0, 'T':0, 'RT':1, 'LT':-1, 'RB':1, 'LB':-1}

king, stone, N = input().split()
kr, kc = 8-int(king[1]), ord(king[0])-65
pan[kr][kc] = 1
sr, sc = 8-int(stone[1]), ord(stone[0])-65
pan[sr][sc] = 2
for _ in range(int(N)):
    move = input()
    nr = kr + dr[move]
    nc = kc + dc[move]
    ok = True
    if 0 <= nr < 8 and 0 <= nc < 8:
        if pan[nr][nc]:
            nsr = sr+dr[move]
            nsc = sc+dc[move]
            if 0 <= nsr < 8 and 0 <= nsc < 8:
                pan[nr][nc] = 0
                pan[nsr][nsc] = 2
                sr, sc = nsr, nsc
            else:
                ok = False
        if ok:
            pan[kr][kc] = 0
            pan[nr][nc] = 1
            kr, kc = nr, nc

print(chr(kc+65), 8-kr, sep='')
print(chr(sc+65), 8-sr, sep='')