import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        I = input()
        if 'S' in I:
            print(I)
            return


if __name__ == '__main__':
    main()