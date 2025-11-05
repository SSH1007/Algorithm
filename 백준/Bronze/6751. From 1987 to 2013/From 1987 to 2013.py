import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    Y = int(input())
    while 1:
        Y += 1
        if len(set(str(Y))) == len(str(Y)):
            break
    print(Y)


if __name__ == '__main__':
    main()