import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    N = len(S)
    lst = [0]*N
    lst[0] = 1
    for n in range(1, N):
        if S[n] > S[n-1]:
            lst[n] = lst[n-1]+1
        else:
            lst[n] = 1
    print(sum(lst))


if __name__ == '__main__':
    main()