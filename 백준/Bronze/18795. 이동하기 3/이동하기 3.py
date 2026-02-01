import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _, _ = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(sum(A)+sum(B))


if __name__ == '__main__':
    main()