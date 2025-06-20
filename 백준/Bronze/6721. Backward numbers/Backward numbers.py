import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        a, b = input().split()
        print(int(str(int(a[::-1])+int(b[::-1]))[::-1]))


if __name__ == '__main__':
    main()