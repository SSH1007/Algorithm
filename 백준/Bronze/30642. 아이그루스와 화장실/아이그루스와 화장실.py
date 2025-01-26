import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    mascot = input()
    K = int(input())
    if mascot == 'induck':
        if K%2 == 0:
            print(K)
        else:
            if K+1 > N:
                print(K-1)
            else:
                print(K+1)
    else:
        if K%2:
            print(K)
        else:
            if K+1 > N:
                print(K-1)
            else:
                print(K+1)


if __name__ == '__main__':
    main()