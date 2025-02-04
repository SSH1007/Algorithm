import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    cur = list(map(int, input().split(':')))
    bot = list(map(int, input().split(':')))
    curS = cur[0]*3600+cur[1]*60+cur[2]
    botS = bot[0]*3600+bot[1]*60+bot[2]
    c = botS-curS
    if c == 0:
        print('24:00:00')
        return 0
    h = str((c//3600)%24)
    m = str((c%3600)//60)
    s = str((c%3600)%60)
    print(f'{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}')


if __name__ == '__main__':
    main()