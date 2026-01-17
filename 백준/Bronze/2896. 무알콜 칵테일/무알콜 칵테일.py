import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B, C = map(int, input().split())
    I, J, K = map(int, input().split())
    tmp = min(A/I, B/J, C/K)
    A = A-I*tmp
    B = B-J*tmp
    C = C-K*tmp
    print(A, B, C)


if __name__ == '__main__':
    main()