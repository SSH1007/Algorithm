import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = []
    i = 1
    while 1:
        I = i*i*i
        if I > 2000000000:
            break
        lst.append(I)
        i += 1
    T = int(input())
    for x in range(1, T+1):
        A, B = map(int, input().split())
        M = 0
        for l in lst:
            if A <= l <= B:
                M += 1
        print(f'Case #{x}: {M}')


if __name__ == '__main__':
    main()