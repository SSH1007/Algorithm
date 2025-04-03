import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(N):
        if n > 0:
            print()
        X = int(input())
        lst = []
        for i in range(1, X//2+1):
            if X%i == 0:
                lst.append(i)
        Y = sum(lst)
        if Y > X:
            print(f'{X} is an abundant number.')
        elif Y == X:
            print(f'{X} is a perfect number.')
        else:
            print(f'{X} is a deficient number.')


if __name__ == '__main__':
    main()