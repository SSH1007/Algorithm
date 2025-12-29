import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a = int(input())
    j, u = map(int, input().split())
    dap = 100
    if j/a*2 <= u:
        dap = min(dap, j/a*2)
    if j/a*2 > u:
        dap = min(dap, max(j, u))
    if j >= u/a*2:
        dap = min(dap, u/a*2)
    if j < u/a*2:
        dap = min(dap, max(j, u))
    print(dap)


if __name__ == '__main__':
    main()