N = int(input())
Ascore, Bscore = 0, 0
info = [(0, 0)]
dic = {0: 0, 1: 0, 2: 0}
for _ in range(N):
    team, time = input().split()
    team = int(team)
    m, s = map(int, time.split(':'))
    info.append((team, m*60+s))
info.append((0, 48*60))
for i in range(1, N+2):
    overwhelming = info[i][1] - info[i-1][1]
    if Ascore > Bscore:
        dic[1] += overwhelming
    elif Ascore < Bscore:
        dic[2] += overwhelming
    if info[i][0] == 1:
        Ascore += 1
    else:
        Bscore += 1

Am, As = dic[1]//60, dic[1] % 60
Bm, Bs = dic[2]//60, dic[2] % 60
print(str(Am).zfill(2), ':', str(As).zfill(2), sep='')
print(str(Bm).zfill(2), ':', str(Bs).zfill(2), sep='')