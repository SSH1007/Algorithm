import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        lst = [input() for _ in range(H)]
        for i in range(H-1, -1, -1):
            print(lst[i])


if __name__ == '__main__':
    main()