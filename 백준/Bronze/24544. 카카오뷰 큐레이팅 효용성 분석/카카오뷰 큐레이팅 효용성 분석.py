import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    print(sum(As))
    tmp = 0
    for n in range(N):
        tmp += (Bs[n]^1)*As[n]
    print(tmp)


if __name__ == '__main__':
    main()