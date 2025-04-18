import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = input()
    K = input()
    tmp = ''
    for n in N:
        if not n.isdigit():
            tmp += n
    if K in tmp:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()