import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    M, H = map(int, input().split())
    dap = 0
    for _ in range(int(input())):
        C, B = map(int, input().split())
        dap += C*M if C*M > B*H else B*H
    print(dap)


if __name__ == '__main__':
    main()