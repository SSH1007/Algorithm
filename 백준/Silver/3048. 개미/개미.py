import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N1, N2 = map(int, input().split())
    first = list(input())[::-1]
    second = list(input())
    T = int(input())
    ants = first+second
    for _ in range(T):
        i = 0
        while i < len(ants):
            if ants[i] in first:
                if i < N1+N2-1:
                    if ants[i+1] in second:
                        ants[i], ants[i+1] = ants[i+1], ants[i]
                        i += 1
            i += 1
    print(*ants, sep='')


if __name__ == '__main__':
    main()