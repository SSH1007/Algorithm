import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    b = [1, 0, 0]
    for s in S:
        if s == 'A':
            b[0], b[1] = b[1], b[0]
        elif s == 'B':
            b[1], b[2] = b[2], b[1]
        else:
            b[0], b[2] = b[2], b[0]
    print(b.index(1)+1)


if __name__ == '__main__':
    main()