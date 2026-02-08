import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _, _ = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    dap = sum(As)
    for b in Bs:
        if b == 0:
            continue
        dap *= b
    print(dap)


if __name__ == '__main__':
    main()