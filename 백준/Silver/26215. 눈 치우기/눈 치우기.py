import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    As = sorted(list(map(int, input().split())))
    dap = 0
    while len(As) > 1:
        a = As.pop()
        b = As.pop()
        if a-1 > 0:
            As.append(a-1)
        if b-1 > 0:
            As.append(b-1)
        As.sort()
        dap += 1
    As.append(0)
    if dap + As[0] > 1440:
        print(-1)
    else:
        print(dap+As[0])


if __name__ == '__main__':
    main()