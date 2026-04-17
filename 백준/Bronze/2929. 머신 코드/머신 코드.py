import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    C = input()
    plus, dap = 0, 0
    for i in range(len(C)):
        if C[i].isupper():
            if (i+plus) % 4 != 0:
                plus += -(i+plus)%4
    print(plus)


if __name__ == '__main__':
    main()