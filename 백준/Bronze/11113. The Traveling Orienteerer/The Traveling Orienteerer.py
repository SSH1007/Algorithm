import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    xy = []
    for _ in range(n):
        x, y = map(float, input().split())
        xy.append((x, y))
    m = int(input())
    for _ in range(m):
        p = int(input())
        lst = list(map(int, input().split()))
        dap = 0
        for i in range(p-1):
            L = (xy[lst[i]][0]-xy[lst[i+1]][0])**2 + (xy[lst[i]][1]-xy[lst[i+1]][1])**2
            dap += L**0.5
        print(int(dap) if dap%1 < 0.5 else int(dap) + 1)


if __name__ == '__main__':
    main()