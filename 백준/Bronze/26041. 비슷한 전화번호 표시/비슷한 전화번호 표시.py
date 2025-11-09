import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    As = list(input().split())
    dap = 0
    B = input()
    for A in As:
        if len(A) > len(B) and A[:len(B)] == B:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()