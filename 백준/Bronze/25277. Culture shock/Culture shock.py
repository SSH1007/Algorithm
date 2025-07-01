import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    W = list(input().split())
    dap = 0
    for w in W:
        if w in ['he', 'him', 'she', 'her']:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()