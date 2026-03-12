import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        l = len(S)//3+1 if (len(S)/3)%1 else len(S)//3
        Sd = S[:l]
        if S == Sd+Sd[::-1]+Sd:
            print(1)
        elif S == Sd+Sd[::-1][1:]+Sd:
            print(1)
        elif S == Sd+Sd[::-1]+Sd[1:]:
            print(1)
        elif S == Sd+Sd[::-1][1:]+Sd[1:]:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()