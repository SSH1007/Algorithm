import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        print(k*23)


if __name__ == '__main__':
    main()