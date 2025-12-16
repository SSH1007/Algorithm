import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        f, l, n = 0, 0, 0
        flag = False
        for i in range(len(S)):
            if S[i].isdecimal():
                flag = True
                n = int(S[i])
            elif flag:
                f += 1
            else:
                l += 1
        if f > 0:
            n = 1
        if l%2:
            n = abs(n-1)
        print(n)


if __name__ == '__main__':
    main()