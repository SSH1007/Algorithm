import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        L, R, S = map(int, input().split())
        s, i = 1, 1
        while 1:
            if S == L or S == R:
                break
            if i%2:
                S+=i
            else:
                S-=i
            i += 1
            s += 1
        print(s)


if __name__ == '__main__':
    main()