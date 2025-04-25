import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    sH, sM = map(int, input().split())
    eH, eM = map(int, input().split())
    N = input()
    dap = 0
    while 1:
        tmp = str(sH)+str(sM)
        for t in tmp.zfill(4):
            if t == N:
                dap += 1
                break
        if eH == sH and eM == sM:
            break
        sM += 1
        if sM == 60:
            sH += 1
            sM = 0
    print(dap)


if __name__ == '__main__':
    main()