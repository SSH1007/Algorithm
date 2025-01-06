import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A = input()
    B = input()
    C = input()
    print(int(A)+int(B)-int(C))
    print(int(A+B)-int(C))


if __name__ == '__main__':
    main()