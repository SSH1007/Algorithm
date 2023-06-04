import sys
input = sys.stdin.readline
cnt = 1
while 1:
    L, P, V = map(int, input().rstrip().split())
    if L+P+V == 0:
        break
    weeks = V//P
    usableDays = weeks*L
    restDays = V%P
    print(f'Case {cnt}: {usableDays+min(L, restDays)}')
    cnt += 1