import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    HP = list(map(int, input().split()))
    # 숫자 맞추기
    for _ in range(3-N):
        HP.append(0)
    s = set()
    check = [[[0]*61 for _ in range(61)] for _ in range(61)]

    def mutalisk(a, b, c, cnt):
        if a < 0:
            a = 0
        if b < 0:
            b = 0
        if c < 0:
            c = 0
        tmp = sorted([a, b, c], reverse=True)
        a, b, c = tmp[0], tmp[1], tmp[2]
        if check[a][b][c] and a+b+c != 0:
            return
        check[a][b][c] = 1
        if a+b+c == 0:
            s.add(cnt)
            return

        mutalisk(a-9, b-3, c-1, cnt+1)
        mutalisk(a-9, b-1, c-3, cnt+1)
        mutalisk(a-3, b-9, c-1, cnt+1)
        mutalisk(a-1, b-9, c-3, cnt+1)
        mutalisk(a-3, b-1, c-9, cnt+1)
        mutalisk(a-1, b-3, c-9, cnt+1)

    mutalisk(HP[0], HP[1], HP[2], 0)
    print(min(s))


if __name__ == '__main__':
    main()