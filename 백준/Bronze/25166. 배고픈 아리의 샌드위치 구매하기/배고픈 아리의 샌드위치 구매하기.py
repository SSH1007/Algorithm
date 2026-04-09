import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S, M = map(int, input().split())
    if S <= 1023:
        print('No thanks')
    else:
        need = S-1023
        n2 = bin(need)
        M2 = bin(M)
        if int(n2[2:], 2)&int(M2[2:], 2) != need:
            print('Impossible')
        else:
            print('Thanks')


if __name__ == '__main__':
    main()