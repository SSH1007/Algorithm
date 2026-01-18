import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    sch = [0]*1000
    lst = []
    dap = 0
    N = int(input())
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))
        for i in range(a, b):
            sch[i] += 1
    for l in lst:
        a, b = l
        for i in range(a, b):
            sch[i] -= 1
        dap = max(dap, sum(s != 0 for s in sch))
        for i in range(a, b):
            sch[i] += 1
    print(dap)


if __name__ == '__main__':
    main()