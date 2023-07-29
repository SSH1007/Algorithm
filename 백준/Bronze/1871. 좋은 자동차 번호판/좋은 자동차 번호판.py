dic = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = int(input())
for _ in range(N):
    front, end = input().split('-')
    end = int(end)
    fNum = 0
    for n in range(len(front)-1, -1, -1):
        fNum += dic.index(front[len(front)-n-1])*(26**n)
    if abs(fNum-end) <= 100:
        print('nice')
    else:
        print('not nice')