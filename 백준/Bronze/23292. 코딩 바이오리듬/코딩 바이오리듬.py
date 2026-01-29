import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    birth = list(map(int, input()))
    N = int(input())
    dap = []
    for _ in range(N):
        date = input()
        date_ = list(map(int, date))
        y, m, d = 0, 0, 0
        for i in range(4):
            y += (birth[i]-date_[i])**2
        for i in range(4, 6):
            m += (birth[i]-date_[i])**2
        for i in range(6, 8):
            d += (birth[i]-date_[i])**2
        dap.append((int(date), y*m*d))
    print(sorted(dap, key=lambda x: (-x[1], x[0]))[0][0])


if __name__ == '__main__':
    main()