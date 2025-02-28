import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    c = min(a, b)
    for i in range(1, c+1):
        if a%i==0 and b%i==0:
            print(i, a//i, b//i)


if __name__ == '__main__':
    main()