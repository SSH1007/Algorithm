import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        L, R, S = map(int, input().split())
        LS, RS = abs(L-S), abs(R-S)
        if S == R or S == L:
            print(0)
            continue
        if LS > RS:
            print(RS*2)
        elif LS < RS:
            print(LS*2+1)
        else:
            print(RS*2)


if __name__ == '__main__':
    main()