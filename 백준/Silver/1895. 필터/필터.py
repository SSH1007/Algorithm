import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    R, C = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(R)]
    T = int(input())
    lst, cnt = [], 0
    for r in range(R-2):
        for c in range(C-2):
            tmp = []
            for i in range(3):
                for j in range(3):
                    tmp.append(maps[r+i][c+j])
            if sorted(tmp)[4] >= T:
                cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()