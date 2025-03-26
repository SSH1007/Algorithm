import sys
input = lambda: sys.stdin.readline().rstrip()


def check(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def main():
    O, N = input().split()
    A, B = check(int(O)), check(int(N+O))
    if A == B:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()